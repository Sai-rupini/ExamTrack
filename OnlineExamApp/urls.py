from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    index, student_register, teacher_register, admin_register, 
    user_login, user_logout, student_dashboard, teacher_dashboard, admin_dashboard,view_exams,take_exam,view_results,create_exam,view_students_and_results,upload_material,view_study_materials,edit_student_profile,manage_students,manage_teachers,edit_student,edit_teacher
    
)

urlpatterns = [
    path('', index, name='index'),
    path('register/student/', student_register, name='student_register'),
    path('register/teacher/', teacher_register, name='teacher_register'),
    path('register/admin/', admin_register, name='admin_register'),

    path('login/student/', lambda request: user_login(request, 'student'), name='student_login'),
    path('login/teacher/', lambda request: user_login(request, 'teacher'), name='teacher_login'),
    path('login/admin/', lambda request: user_login(request, 'admin'), name='admin_login'),

    path('logout/', user_logout, name='logout'),

    # ✅ Dashboard URLs
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
    path('student/view-exams/', view_exams, name='student_view_exams'),
    path('student/take-exam/<int:exam_id>/', take_exam, name='student_take_exam_detail'),
    path('student/view-materials/', view_study_materials, name='view_materials'),
    path('student/edit-profile/', edit_student_profile, name='edit_student_profile'),
    path('student/view-results/', view_results, name='student_view_results'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/create-exam/', create_exam, name='create_exam'),
    path('teacher/view-students/', view_students_and_results, name='view_students_results'),
    path('teacher/upload-material/', upload_material, name='upload_material'),



    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('manage-students/', manage_students, name='manage_students'),
    path('manage-students/<int:student_id>/edit/',edit_student, name='edit_student'),
    
    path('manage-teachers/', manage_teachers, name='manage_teachers'),
    path('manage-teachers/<int:teacher_id>/edit/', edit_teacher, name='edit_teacher'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
