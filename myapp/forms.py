
from myapp.models.teacher import Teacher
from myapp.models.theory import Theory
from django.forms import ModelForm, TextInput, Textarea, ImageField, Select, SelectMultiple
from django import forms

from myapp.models.user import User


class ModuleForm(ModelForm):
    class Meta:
        model = Theory
        fields = ["title", "content", "image", "video_url"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
            # "image": FileInput(attrs={
            #     'class': 'form-control'
            # }),
        }


class StudentRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "password"]


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class StudentLoginForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get('password')

        try:
            student = User.objects.get(first_name=first_name, last_name=last_name)
            if student.password != password:
                raise forms.ValidationError("Incorrect password")
        except User.DoesNotExist:
            raise forms.ValidationError("Student not found")

        return cleaned_data




# class QuizForm(forms.Form):
#     user_answer = forms.CharField(label='Answer', max_length=200)
#
