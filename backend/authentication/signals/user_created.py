from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.encoding import force_bytes 
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from ..models import UserModified

from .generate_tokens import account_activation_token

from core.settings.settings import SCHEME, DOMAIN


@receiver(post_save, sender=UserModified)
def send_confiration_email(sender, instance, created, **kwargs):    
    if created and not instance.is_active:
        email = instance.email
        subject = "Email Verification"
        message = render_to_string('user/verification_email.html', {
            'scheme': SCHEME,
            'user': instance,
            'domain': DOMAIN,
            'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
            'token': account_activation_token.make_token(instance),
        })
        email = EmailMessage(
            subject, message, to=[email]
        )
        email.content_subtype = 'html'
        email.send()
