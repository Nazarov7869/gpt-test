from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Appeal, UserProfile


class StyledAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login yoki email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parolingiz'}))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Ism')
    last_name = forms.CharField(max_length=100, label='Familiya')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Telefon')
    region = forms.CharField(max_length=100, label='Viloyat')
    gender = forms.ChoiceField(choices=UserProfile.Gender.choices, label='Jinsi')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'region', 'gender', 'password1', 'password2')


class AppealCreateForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('category', 'recipient', 'module', 'subject', 'body', 'attachment')
        widgets = {
            'category': forms.Select(),
            'module': forms.TextInput(attrs={'placeholder': "Masalan: O'quv jarayoni"}),
            'subject': forms.TextInput(attrs={'placeholder': 'Qisqa mavzu kiriting'}),
            'body': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Murojaat mazmuni'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient'].queryset = User.objects.filter(
            is_staff=True,
            profile__role__in=[
                UserProfile.Role.SUPERADMIN,
                UserProfile.Role.RECTOR,
                UserProfile.Role.DEAN,
                UserProfile.Role.PRORECTOR,
            ],
        ).select_related('profile')
        self.fields['recipient'].label_from_instance = lambda u: f"{u.get_full_name() or u.username} ({u.profile.get_role_display()})"


class AppealModerationForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ('status', 'admin_comment')
        widgets = {
            'admin_comment': forms.Textarea(attrs={'rows': 4}),
        }
