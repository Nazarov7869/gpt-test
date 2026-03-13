from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    class Role(models.TextChoices):
        APPLICANT = 'applicant', 'Talaba/Fuqaro'
        SUPERADMIN = 'superadmin', 'Superadmin'
        RECTOR = 'rektor', 'Rektor'
        DEAN = 'dekan', 'Dekan'
        PRORECTOR = 'prorektor', 'Prorektor'

    class Gender(models.TextChoices):
        MALE = 'male', 'Erkak'
        FEMALE = 'female', 'Ayol'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.APPLICANT)
    phone = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


class Appeal(models.Model):
    class Category(models.TextChoices):
        APPEAL = 'appeal', 'Murojaat'
        APPLICATION = 'application', 'Ariza'
        SUGGESTION = 'suggestion', 'Taklif'
        COMPLAINT = 'complaint', 'Shikoyat'

    class Status(models.TextChoices):
        NEW = 'new', 'Yangi'
        VIEWED = 'viewed', "Ko'rib chiqilgan"
        IN_REVIEW = 'in_review', "Ko'rilmoqda"
        ANSWERED = 'answered', 'Javob berilgan'
        REJECTED = 'rejected', 'Rad etilgan'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appeals')
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='received_appeals',
        help_text='Qabul qiluvchi xodim',
    )
    category = models.CharField(max_length=20, choices=Category.choices)
    module = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=180)
    body = models.TextField()
    attachment = models.FileField(upload_to='appeals/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    admin_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} -> {self.recipient.username}: {self.subject}"
