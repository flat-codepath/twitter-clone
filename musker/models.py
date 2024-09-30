from django.db import models
from django.contrib.auth.models import User


# Create a User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fallows = models.ManyToManyField("self", related_name='fallowed_by',
                                     symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username



