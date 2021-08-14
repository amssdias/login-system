from django.test import SimpleTestCase
from django.urls import reverse, resolve
from loginSys.views import register, _login, _logout, main, activate_account

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

    def test_activate_account(self):
        url = reverse('activate_account', kwargs={'uidb64': 'MTE', 'token': 'abcde123'})
        self.assertEqual(resolve(url).func, activate_account)
        self.assertEqual(resolve(url).kwargs['uidb64'], 'MTE')
        self.assertEqual(resolve(url).kwargs['token'], 'abcde123')
        self.assertEqual(resolve(url).url_name, 'activate_account')
        self.assertEqual(resolve(url).route, 'activate_account/<uidb64>/<token>')

