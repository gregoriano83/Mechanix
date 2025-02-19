from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    company = models.CharField(max_length=255)
    email = models.EmailField()
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    contact_reference = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' % self.company
    
@receiver(post_save, sender=User)
def default_to_non_active(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff == False:
            instance.is_active = False
            client = Client.objects.create(
                email=instance.username,
                company=instance.first_name,
                created_by=instance
            )        
            client.save()
            instance.save()
