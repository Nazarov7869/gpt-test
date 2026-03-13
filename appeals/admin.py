from django.contrib import admin

from .models import Appeal, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'region')
    list_filter = ('role', 'gender')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'user', 'recipient', 'category', 'status', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('subject', 'body', 'user__username', 'recipient__username')
