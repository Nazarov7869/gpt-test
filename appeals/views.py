from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdminAppealForm, AppealForm, RegisterForm
from .models import Appeal


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Ro\'yxatdan o\'tdingiz. Endi tizimga kiring.')
        return redirect('login')
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    form = AppealForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        appeal = form.save(commit=False)
        appeal.owner = request.user
        appeal.save()
        messages.success(request, 'Murojaatingiz qabul qilindi.')
        return redirect('dashboard')

    appeals = Appeal.objects.filter(owner=request.user)
    return render(request, 'appeals/dashboard.html', {'form': form, 'appeals': appeals})


@login_required
def appeal_detail(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk, owner=request.user)
    return render(request, 'appeals/appeal_detail.html', {'appeal': appeal})


def staff_required(view):
    return user_passes_test(lambda user: user.is_authenticated and user.is_staff)(view)


@staff_required
def admin_appeals(request):
    appeals = Appeal.objects.select_related('owner').all()
    return render(request, 'appeals/admin_appeals.html', {'appeals': appeals})


@staff_required
def admin_appeal_edit(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    form = AdminAppealForm(request.POST or None, instance=appeal)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Murojaat yangilandi.')
        return redirect('admin_appeals')
    return render(request, 'appeals/admin_appeal_edit.html', {'form': form, 'appeal': appeal})


@staff_required
def admin_appeal_delete(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    if request.method == 'POST':
        appeal.delete()
        messages.success(request, 'Murojaat o\'chirildi.')
        return redirect('admin_appeals')
    return render(request, 'appeals/admin_appeal_delete.html', {'appeal': appeal})
