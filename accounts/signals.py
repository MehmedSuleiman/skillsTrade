from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string
from .models import Profile

from schools.models import School

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_pofile(sender, instance, created, **kwargs):
    if created:
        if instance.is_school:
            School.objects.create(user=instance)
        else:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_email_(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.is_school:
        subject = 'Welcome to SkillsTrade for Schools'
        template_name = 'emails/school_registration.html'
    else:
        subject = 'Welcome to SkillsTrade'
        template_name = 'emails/new_user_profile.html'

    html_body = render_to_string(template_name, {'user': instance})
    message = EmailMessage(
        subject=subject,
        body=html_body,
        from_email=settings.COMPANY_EMAIL,
        to=[instance.email],
    )
    message.content_subtype = 'html'
    message.send(fail_silently=True)
