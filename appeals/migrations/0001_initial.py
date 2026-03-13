from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('applicant', 'Talaba/Fuqaro'), ('superadmin', 'Superadmin'), ('rektor', 'Rektor'), ('dekan', 'Dekan'), ('prorektor', 'Prorektor')], default='applicant', max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('appeal', 'Murojaat'), ('application', 'Ariza'), ('suggestion', 'Taklif'), ('complaint', 'Shikoyat')], max_length=20)),
                ('module', models.CharField(blank=True, max_length=150)),
                ('subject', models.CharField(max_length=180)),
                ('body', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='appeals/')),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('viewed', "Ko'rib chiqilgan"), ('in_review', "Ko'rilmoqda"), ('answered', 'Javob berilgan'), ('rejected', 'Rad etilgan')], default='new', max_length=20)),
                ('admin_comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(help_text='Qabul qiluvchi xodim', on_delete=django.db.models.deletion.PROTECT, related_name='received_appeals', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appeals', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
