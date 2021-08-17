from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import UserPasswordResetForm

urlpatterns = [
    path('login/', views._login, name="login"),
    path('logout/', views._logout, name="logout"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),
    path('activate_account/<uidb64>/<token>', views.activate_account, name="activate_account"),
    path('update_password/', views.update_password, name="update_password"),

    # Link to confirm email to reset
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset_form.html", email_template_name="password_reset/password_reset_email.html", form_class=UserPasswordResetForm), name='password_reset'),

    # Email sent
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_done.html"), name='password_reset_done'),

    # Page to write new password
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"), name='password_reset_confirm'),

    # Password reset completed
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"), name='password_reset_complete')
]