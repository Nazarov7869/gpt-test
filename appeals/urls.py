from django.urls import path

from .views import (
    StyledLoginView,
    admin_appeal_delete,
    admin_appeal_edit,
    admin_appeal_list,
    appeal_create,
    dashboard,
    home,
    register,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/login/', StyledLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('appeals/create/', appeal_create, name='appeal_create'),
    path('admin-panel/appeals/', admin_appeal_list, name='admin_appeal_list'),
    path('admin-panel/appeals/<int:pk>/edit/', admin_appeal_edit, name='admin_appeal_edit'),
    path('admin-panel/appeals/<int:pk>/delete/', admin_appeal_delete, name='admin_appeal_delete'),
]
