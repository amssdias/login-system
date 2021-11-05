import logging

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import gettext as _

from smtplib import SMTPException

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('Login System Logger')

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
    try:
        email.send()
    except SMTPException:
        raise ValidationError(_("Email wasn't sent."))