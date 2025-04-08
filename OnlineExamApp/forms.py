from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser,Student,StudyMaterial,Teacher
from django.contrib.auth import get_user_model
class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):  # Ensure email is unique
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'  # Assign user type
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'teacher'  # Assign user type
        if commit:
            user.save()
        return user


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'admin'  # Assign user type
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'
        user.is_active = True  # Ensure account is active
        user.set_password(self.cleaned_data["password1"])  # Properly hash password
        if commit:
            user.save()
            Student.objects.create(user=user)
        return user
class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['title', 'description', 'file']
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
CustomUser = get_user_model()

class StudentEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ['user']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        if self.user_instance:
            self.fields['email'].initial = self.user_instance.email

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user_instance:
            self.user_instance.email = self.cleaned_data['email']
            if commit:
                self.user_instance.save()
        if commit:
            instance.save()
        return instance

class TeacherEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ['user']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        if self.user_instance:
            self.fields['email'].initial = self.user_instance.email

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user_instance:
            self.user_instance.email = self.cleaned_data['email']
            if commit:
                self.user_instance.save()
        if commit:
            instance.save()
        return instance