from logging import log
from loginSys.views import register
from django.test import TransactionTestCase 
from loginSys.forms import LoginForm, RegisterForm


class TestForm(TransactionTestCase):

    def test_login_form_valid_data(self):
        login_form = LoginForm(data={
            'username': 'andre',
            'password': 'diasdias'
        })

        self.assertTrue(login_form.is_valid())

    def test_login_form_invalid_data(self):
        login_form = LoginForm(data={})

        self.assertFalse(login_form.is_valid())
        self.assertEquals(len(login_form.errors), 2)

    def test_register_form_valid_data(self):
        register_form = RegisterForm(data={
            'first_name': 'andre',
            'last_name': 'dias',
            'username': 'AndreDias',
            'email': 'andre@gmail.com',
            'password': 'diasdias',
            'password_confirmation': 'diasdias'
        })

        self.assertTrue(register_form.is_valid())

    def test_register_form_invalid_data(self):
        register_form = RegisterForm(data={})
        self.assertFalse(register_form.is_valid())

        register_form = RegisterForm(data={
            'first_name': 'andre',
            'last_name': 'dias',
            'username': 'AndreDias',
            'password': 'diasdias',
            'password_confirmation': 'dias',
            'email': 'andre@notvalid.com'
        })

        self.assertFalse(register_form.is_valid())
        self.assertEquals(len(register_form.errors), 2)