import json
from django.test import TestCase, Client
from .models import User
from django.contrib.auth import get_user_model

client = Client()


class RegisterTest(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_register_post_success(self):
        register_info = {
            "email": "tommorrow@tommorrow.io",
            "name": "tommorrow",
            "password": "qwer123!!!",
        }
        response = client.post(
            "/auth/register/",
            json.dumps(register_info),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_register_post_invalid_password(self):
        register_info = {
            "email": "test@test.io",
            "name": "test",
            "password": "1234567",
        }
        response = client.post(
            "/auth/register/",
            json.dumps(register_info),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_register_post_invalid_email(self):
        register_info = {
            "email": "test@testio",
            "name": "test",
            "password": "test123!!!",
        }
        response = client.post(
            "/auth/register/",
            json.dumps(register_info),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
