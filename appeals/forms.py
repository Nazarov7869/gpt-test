from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appeal


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('full_name', 'phone', 'subject', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }


class AdminAppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('status', 'admin_note')
        widgets = {
            'admin_note': forms.Textarea(attrs={'rows': 4}),
        }
