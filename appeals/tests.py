from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Appeal


class AccessTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user1', password='secret123')
        self.other = User.objects.create_user(username='user2', password='secret123')
        self.admin = User.objects.create_user(username='admin', password='secret123', is_staff=True)
        self.appeal = Appeal.objects.create(
            owner=self.user,
            full_name='Ali Valiyev',
            phone='+998901112233',
            subject='Test mavzu',
            body='Test matn',
        )

    def test_user_only_sees_own_appeal(self):
        self.client.login(username='user2', password='secret123')
        response = self.client.get(reverse('appeal_detail', args=[self.appeal.id]))
        self.assertEqual(response.status_code, 404)

    def test_only_admin_accesses_admin_panel(self):
        self.client.login(username='user1', password='secret123')
        response = self.client.get(reverse('admin_appeals'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='secret123')
        response = self.client.get(reverse('admin_appeals'))
        self.assertEqual(response.status_code, 200)
