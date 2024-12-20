from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create a Meep Model:
class Meep(models.Model):
    user = models.ForeignKey(User, related_name='meeps', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='meep_like', blank=True)

    # keep track of likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f'{self.user}'",     "
            f'{self.created_at:%y-%m-%d %H:%M}'",     "
            f'{self.body}'
        )


# Create a User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fallows = models.ManyToManyField("self", related_name='fallowed_by',
                                     symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100)
    linkedin_like = models.CharField(null=True, blank=True, max_length=100)

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
