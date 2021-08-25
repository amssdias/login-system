from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_password(value):
    if len(value) < 8:
        raise ValidationError(_("Password must be 8 characters minimum"))
    return value


domain_emails = ['gmail.com', 'hotmail.com']
def validate_domain_email(value):
    if "@" not in value:
        raise ValidationError(_("Must provide a valid email."))

    domain = value.split("@")[1]
    if domain not in domain_emails:
        raise ValidationError(_("Email not valid. Available domain names: 'hotmail' or 'gmail'."))

    return value