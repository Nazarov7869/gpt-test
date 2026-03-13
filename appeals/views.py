from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppealCreateForm, AppealModerationForm, RegisterForm, StyledAuthenticationForm
from .models import Appeal, UserProfile


class StyledLoginView(LoginView):
    form_class = StyledAuthenticationForm
    template_name = 'registration/login.html'


def is_admin(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    if not user.is_staff:
        return False
    return getattr(user, 'profile', None) and user.profile.role in {
        UserProfile.Role.SUPERADMIN,
        UserProfile.Role.RECTOR,
        UserProfile.Role.DEAN,
        UserProfile.Role.PRORECTOR,
    }


def home(request):
    return render(request, 'appeals/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = UserProfile.Role.APPLICANT
        profile.phone = form.cleaned_data['phone']
        profile.region = form.cleaned_data['region']
        profile.gender = form.cleaned_data['gender']
        profile.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    my_appeals = Appeal.objects.filter(user=request.user)
    status_stats = my_appeals.values('status').annotate(total=Count('id'))
    status_map = {item['status']: item['total'] for item in status_stats}
    context = {
        'appeals': my_appeals.select_related('recipient'),
        'appeals_total': my_appeals.count(),
        'appeals_new': status_map.get(Appeal.Status.NEW, 0),
        'appeals_in_review': status_map.get(Appeal.Status.IN_REVIEW, 0),
        'appeals_viewed': status_map.get(Appeal.Status.VIEWED, 0),
        'appeals_answered': status_map.get(Appeal.Status.ANSWERED, 0),
        'profile': getattr(request.user, 'profile', None),
    }
    return render(request, 'appeals/dashboard.html', context)


@login_required
def appeal_create(request):
    form = AppealCreateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        appeal = form.save(commit=False)
        appeal.user = request.user
        appeal.save()
        messages.success(request, 'Murojaatingiz muvaffaqiyatli yuborildi.')
        return redirect('dashboard')
    return render(request, 'appeals/appeal_form.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def admin_appeal_list(request):
    appeals = Appeal.objects.select_related('user', 'recipient').all()
    return render(request, 'appeals/admin_appeal_list.html', {'appeals': appeals})


@login_required
@user_passes_test(is_admin)
def admin_appeal_edit(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    if appeal.status == Appeal.Status.NEW:
        appeal.status = Appeal.Status.VIEWED
        appeal.save(update_fields=['status'])
    form = AppealModerationForm(request.POST or None, instance=appeal)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Murojaat yangilandi.')
        return redirect('admin_appeal_list')
    return render(request, 'appeals/admin_appeal_edit.html', {'appeal': appeal, 'form': form})


@login_required
@user_passes_test(is_admin)
def admin_appeal_delete(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    if request.method == 'POST':
        appeal.delete()
        messages.success(request, "Murojaat o'chirildi.")
        return redirect('admin_appeal_list')
    return render(request, 'appeals/admin_appeal_delete.html', {'appeal': appeal})
