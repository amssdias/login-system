from django.contrib.auth import views as auth_views
from django.urls import path, include

from loginSys.forms import UserPasswordResetForm, UserSetPassword
from loginSys.views import ( 
    ActivateAccount, 
    LoginUser, 
    LogoutUser, 
    MainView, 
    RegisterUser, 
    UpdatePassword
)


password_reset_patterns = [
    path('update_password/', UpdatePassword.as_view(), name="update_password"),

    # Link to confirm email to reset
    path('password_reset', 
        auth_views.PasswordResetView.as_view(
            template_name="password_reset/password_reset_form.html", 
            email_template_name="password_reset/password_reset_email.html", 
            form_class=UserPasswordResetForm), 
        name='password_reset'),

    # Email sent
    path('password_reset_done', 
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset/password_reset_done.html"),
        name='password_reset_done'),

    # Page to write new password
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset/password_reset_confirm.html", 
            form_class=UserSetPassword), 
        name='password_reset_confirm'),

    # Password reset completed
    path('password_reset_complete', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset/password_reset_complete.html"), 
        name='password_reset_complete')
]

authentication_patterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('activate_account/<uidb64>/<token>', ActivateAccount.as_view(), name="activate_account"),
]

urlpatterns = [
    path('auth/', include(authentication_patterns)),
    path('password/', include(password_reset_patterns)),
    path('main/', MainView.as_view(), name="main"),
]
