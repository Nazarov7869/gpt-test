from django.contrib import admin

from .models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'owner', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'body', 'owner__username')
