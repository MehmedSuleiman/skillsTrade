from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Profile

from schools.models import School

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_pofile(sender, instance, created, **kwargs) -> HttpResponse:
    if created:
        if instance.is_school:
            School.objects.create(user=instance)
            return redirect('schools:update_school')
        else:
            Profile.objects.create(user=instance)
            return redirect('schools:update_school') #TODO: to be fixed when the url for profile creation is made.

    else:
        return HttpResponse(status=404)