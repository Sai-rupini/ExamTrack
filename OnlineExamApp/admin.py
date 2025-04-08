from django.contrib import admin
from .models import CustomUser, Student, Teacher, Admin,Exam, Question, Result,StudyMaterial

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'created_by')
    inlines = [QuestionInline]

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'score', 'date_taken')
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False

class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
class CustomUserAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ('username', 'email', 'user_type')

    def get_inline_instances(self, request, obj=None):
        if obj and obj.user_type == 'student':
            return [StudentInline(self.model, self.admin_site)]
        elif obj and obj.user_type == 'teacher':
            return [TeacherInline(self.model, self.admin_site)]
        return []

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question)
admin.site.register(Result, ResultAdmin)
admin.site.register(StudyMaterial)
