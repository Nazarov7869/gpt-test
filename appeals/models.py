from django.conf import settings
from django.db import models


class Appeal(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Yangi'
        IN_REVIEW = 'in_review', "Ko'rib chiqilmoqda"
        ANSWERED = 'answered', 'Javob berilgan'
        REJECTED = 'rejected', 'Rad etilgan'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appeals')
    subject = models.CharField(max_length=180)
    body = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    admin_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.subject}"
