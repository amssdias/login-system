from django.test import SimpleTestCase
from django.urls import reverse, resolve
from loginSys.views import register, _login, _logout, main

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
