from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appeal


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AppealCreateForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('subject', 'body')
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Murojaat mavzusi'}),
            'body': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Murojaat matni'}),
        }


class AppealModerationForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('status', 'admin_comment')
        widgets = {
            'admin_comment': forms.Textarea(attrs={'rows': 4}),
        }
