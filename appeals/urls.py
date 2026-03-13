from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appeals/<int:pk>/', views.appeal_detail, name='appeal_detail'),
    path('admin-panel/appeals/', views.admin_appeals, name='admin_appeals'),
    path('admin-panel/appeals/<int:pk>/edit/', views.admin_appeal_edit, name='admin_appeal_edit'),
    path('admin-panel/appeals/<int:pk>/delete/', views.admin_appeal_delete, name='admin_appeal_delete'),
]
