from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from loginSys.utils import generate_token

from django.test import TestCase, Client
from django.urls import reverse
from loginSys.models import MyUser

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.main = reverse('main')
        self.user_1 = MyUser.objects.create(username='andre')
        self.user_1.set_password('dias1234567')
        self.user_1.save()
        self.activate_account = reverse('activate_account', kwargs={
            'uidb64': urlsafe_base64_encode(force_bytes(self.user_1.pk)),
            'token': generate_token.make_token(self.user_1),
        })
        self.activate_account_false = reverse('activate_account', kwargs={
            'uidb64': '123412',
            'token': 'fake_token',
        })

    
    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginSys/login.html')
    

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginSys/register.html')
    
    
    def test_activate_account_GET(self):
        response = self.client.get(self.activate_account)
        response_wrong = self.client.get(self.activate_account_false)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response_wrong.status_code, 401)
        self.assertTemplateUsed(response_wrong, 'activate_email/failed_activation.html')


    # def test_main_GET(self):
    #     response = self.client.get(self.main)
    #     print(response)

    #     # self.assertEquals(response.status_code, 200)
    #     # self.assertTemplateUsed(response, 'loginSys/index.html')

    def test_register_POST(self):
        
        response_error = self.client.post(self.register_url, {
            'first_name': 'Elizeu',
            'last_name': 'Carlos',
            'email': 'elizeu@gmail.com',
            'password': 'elizeuelizeu',
            'password_confirmation': 'elizeu',
            'username': 'elizeucugi'
        }, secure=True)
        self.assertEqual(response_error.status_code, 400)
        self.assertEqual(MyUser.objects.count(), 1)

        response = self.client.post(self.register_url, {
            'first_name': 'Elizeu',
            'last_name': 'Carlos',
            'email': 'elizeu@gmail.com',
            'password': 'elizeuelizeu',
            'password_confirmation': 'elizeuelizeu',
            'username': 'elizeucugi'
        }, secure=True)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MyUser.objects.count(), 2)
    
    
    def test_login_POST(self):

        response = self.client.post(self.login_url, {
            'username': 'andre',
            'password': 'dias1234567',
        })
        self.assertEqual(response.status_code, 302)