from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserManagerTest(TestCase):
    def test_create_user_success(self):
        user = User.objects.create_user(email='test@example.com', password='pass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('pass123'))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='pass123')

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(email='admin@example.com', password='admin123')
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
