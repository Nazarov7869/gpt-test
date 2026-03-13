from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppealCreateForm, AppealModerationForm, RegisterForm
from .models import Appeal


def is_admin(user):
    return user.is_staff or user.is_superuser


def home(request):
    return render(request, 'appeals/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    appeals = Appeal.objects.filter(user=request.user)
    context = {
        'appeals': appeals,
        'appeals_total': appeals.count(),
        'appeals_answered': appeals.filter(status=Appeal.Status.ANSWERED).count(),
    }
    return render(request, 'appeals/dashboard.html', context)


@login_required
def appeal_create(request):
    form = AppealCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        appeal = form.save(commit=False)
        appeal.user = request.user
        appeal.save()
        messages.success(request, 'Murojaatingiz qabul qilindi.')
        return redirect('dashboard')
    return render(request, 'appeals/appeal_form.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def admin_appeal_list(request):
    appeals = Appeal.objects.select_related('user').all()
    return render(request, 'appeals/admin_appeal_list.html', {'appeals': appeals})


@login_required
@user_passes_test(is_admin)
def admin_appeal_edit(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
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
