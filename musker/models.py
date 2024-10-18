from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create a User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fallows = models.ManyToManyField("self", related_name='fallowed_by',
                                     symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User,auto_now=True)

    def __str__(self):
        return self.user.username


# Create Profile when user Signs Up
# @receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have the user fallow themselves
        user_profile.fallows.set([instance.profile.user.id])



post_save.connect(create_profile, sender=User)
