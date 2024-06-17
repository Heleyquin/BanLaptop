from django.test import TestCase
from django.urls import reverse
from profiles.models import *

class TestSignIn(TestCase):
    def testExistHome(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
    def test_sign_up(self):
        user = {
            'username': 'tk1',
            'email': 'fmdgjndkgdkfm@gmail.com',
            'password1': 'matkhau123',
            'password2': 'matkhau123'
        }
        response = self.client.post(reverse('signup'), user, format='text/html')
        self.assertTemplateUsed(response, 'email/verification.html')
