from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegistrationForm, TeacherRegistrationForm, AdminRegistrationForm, LoginForm,StudentCreationForm,StudyMaterialForm,EditProfileForm,StudentEditForm, TeacherEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import CustomUser,Student,Teacher,Admin, Exam, Question, Result,StudyMaterial
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
def index(request):
    return render(request, 'index.html')

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student registered successfully. Please log in.")
            return redirect('student_login')
        else:
            messages.error(request, "Registration failed. Please check the form fields.")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher registered successfully. Please log in.")
            return redirect('teacher_login')
        else:
            messages.error(request, "Registration failed. Please check the form fields.")
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin registered successfully. Please log in.")
            return redirect('admin_login')
        else:
            messages.error(request, "Registration failed. Please check the form fields.")
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_register.html', {'form': form})

def user_login(request, user_type):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.user_type == user_type:
                login(request, user)
                if user_type == 'student':
                    return redirect('student_dashboard')  # ✅ Ensure URL is defined in urls.py
                elif user_type == 'teacher':
                    return redirect('teacher_dashboard')
                elif user_type == 'admin':
                    return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid credentials for this user type.")
    else:
        form = LoginForm()
    return render(request, f'{user_type}_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

# ✅ Added missing Student Dashboard View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import StudyMaterial, Result

@login_required
def student_dashboard(request):
    user = request.user

    total_materials = StudyMaterial.objects.count()
    student_results = Result.objects.filter(student=user, score__isnull=False)
    
    completed_exams_count = student_results.count()

    passed_exams_count = student_results.filter(score__gte=50).count()
    failed_exams_count = completed_exams_count - passed_exams_count

    avg_score = student_results.aggregate(average_score=Avg('score'))['average_score']

    context = {
        'total_materials': total_materials,
        'completed_exams_count': completed_exams_count,
        'passed_exams_count': passed_exams_count,
        'failed_exams_count': failed_exams_count,
        'avg_score': round(avg_score, 2) if avg_score else 0,
    }

    return render(request, 'student_dashboard.html', context)

def view_exams(request):
    exams = Exam.objects.all()
    return render(request, 'view_exams.html', {'exams': exams})

@login_required
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.questions.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected == question.correct_option:
                score += 1
        percentage = int(score / len(questions) * 100)
        Result.objects.create(student=request.user, exam=exam, score=percentage)
        return redirect('student_view_results')  # ✅ or whatever name your URL pattern uses
    return render(request, 'take_exam.html', {'exam': exam, 'questions': questions})

@login_required
def view_results(request):
    results = Result.objects.filter(student=request.user)
    return render(request, 'view_results.html', {'results': results})
@login_required
def view_study_materials(request):
    materials = StudyMaterial.objects.all()
    return render(request, 'view_materials.html', {'materials': materials})

@login_required
def edit_student_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})
def teacher_dashboard(request):
    exam_count = Exam.objects.count()
    student_count = Student.objects.count()
    return render(request, 'teacher_dashboard.html', {
        'exam_count': exam_count,
        'student_count': student_count
    })


@login_required
def create_exam(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        question_count = int(request.POST.get('question_count', 0))

        # ✅ Fix: include created_by to avoid IntegrityError
        exam = Exam.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )

        # ✅ Save all questions linked to this exam
        for i in range(question_count):
            Question.objects.create(
                exam=exam,
                text=request.POST.get(f'question_{i}'),
                option_a=request.POST.get(f'option_a_{i}'),
                option_b=request.POST.get(f'option_b_{i}'),
                option_c=request.POST.get(f'option_c_{i}'),
                option_d=request.POST.get(f'option_d_{i}'),
                correct_option=request.POST.get(f'correct_option_{i}').upper()
            )

        return redirect('teacher_dashboard')

    return render(request, 'create_exam.html')
@login_required
def view_students_and_results(request):
    if request.user.user_type != 'teacher':
        return redirect('login')  # or show permission denied
    students = Student.objects.all()
    results = Result.objects.select_related('student', 'exam')
    return render(request, 'view_students.html', {
        'students': students,
        'results': results,
    })
from django.contrib import messages

def upload_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Material uploaded successfully!")
    else:
        form = StudyMaterialForm()
    return render(request, 'upload_material.html', {'form': form})






def admin_dashboard(request):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    return render(request, 'admin_dashboard.html', {
        'student_count': student_count,
        'teacher_count': teacher_count
    })

def manage_students(request):
    students = Student.objects.all()
    return render(request, 'manage_students.html', {'students': students})

def manage_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'manage_teachers.html', {'teachers': teachers})
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    user = student.user
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student, user_instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_students')
    else:
        form = StudentEditForm(instance=student, user_instance=user)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    user = teacher.user
    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher, user_instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_teachers')
    else:
        form = TeacherEditForm(instance=teacher, user_instance=user)
    return render(request, 'edit_teacher.html', {'form': form, 'teacher': teacher})