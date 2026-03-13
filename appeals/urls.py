from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appeals/create/', views.appeal_create, name='appeal_create'),
    path('admin-panel/appeals/', views.admin_appeal_list, name='admin_appeal_list'),
    path('admin-panel/appeals/<int:pk>/edit/', views.admin_appeal_edit, name='admin_appeal_edit'),
    path('admin-panel/appeals/<int:pk>/delete/', views.admin_appeal_delete, name='admin_appeal_delete'),
]
