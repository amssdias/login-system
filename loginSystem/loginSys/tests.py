from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from loginSys.views import register, _login, _logout, main
from loginSys.models import MyUser

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, _login)
    
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, _logout)
    
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    
    def test_main_url_resolves(self):
        url = reverse('main')
        self.assertEqual(resolve(url).func, main)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.main = reverse('main')
        self.user_1 = MyUser.objects.create(username='andre')
        self.user_1.set_password('dias1234567')
        self.user_1.save()

    
    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginSys/login.html')
    

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginSys/register.html')


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
