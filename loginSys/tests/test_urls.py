from django.contrib.auth import views as auth_views
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from loginSys.views import (
    RegisterUser,
    LoginUser,
    LogoutUser,
    MainView,
    ActivateAccount,
    UpdatePassword
)


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginUser)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutUser)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterUser)

    def test_main_url_resolves(self):
        url = reverse('main')
        self.assertEqual(resolve(url).func.view_class, MainView)

    def test_activate_account_resolves(self):
        url = reverse('activate_account', kwargs={
                      'uidb64': 'MTE', 'token': 'abcde123'})
        self.assertEqual(resolve(url).func.view_class, ActivateAccount)
        self.assertEqual(resolve(url).kwargs['uidb64'], 'MTE')
        self.assertEqual(resolve(url).kwargs['token'], 'abcde123')
        self.assertEqual(resolve(url).url_name, 'activate_account')
        self.assertEqual(resolve(url).route,
                         'auth/activate_account/<uidb64>/<token>')

    def test_password_update_url_resolves(self):
        url_update_password = reverse('update_password')
        url_password_reset = reverse('password_reset')
        url_password_reset_done = reverse('password_reset_done')
        url_password_reset_confirm = reverse('password_reset_confirm', kwargs={
            'uidb64': 'tre', 'token': 'anothertoken'
        })
        url_password_reset_complete = reverse('password_reset_complete')
        self.assertEqual(resolve(url_update_password).func.view_class, UpdatePassword)
        self.assertEqual(resolve(url_password_reset).func.view_class, auth_views.PasswordResetView)
        self.assertEqual(resolve(url_password_reset_done).func.view_class, auth_views.PasswordResetDoneView)
        self.assertEqual(resolve(url_password_reset_confirm).func.view_class, auth_views.PasswordResetConfirmView)
        self.assertEqual(resolve(url_password_reset_confirm).kwargs['uidb64'], 'tre')
        self.assertEqual(resolve(url_password_reset_confirm).kwargs['token'], 'anothertoken')
        self.assertEqual(resolve(url_password_reset_complete).func.view_class, auth_views.PasswordResetCompleteView)
