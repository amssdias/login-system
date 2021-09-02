from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

class TokenGenerator(PasswordResetTokenGenerator):
    pass

generate_token = TokenGenerator()


def email_activate_account(request, user):
    """
    Send activation link
    """
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    message = render_to_string("activate_email/activate.html", 
    {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": generate_token.make_token(user)
    })

    email = EmailMessage(
        subject=email_subject,
        body=message,
        to=[user.email],
    )

    email.send()