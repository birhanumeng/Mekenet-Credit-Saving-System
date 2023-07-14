from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    """ Create a data model for users """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user_default.png')

    def __str__(self):
        """ print the profile object of name """
        return f"{str(self.user.username)}: {self.role}"

@receiver(post_save,sender=User)
def profileUpdate(sender, instance, created, **kwargs):
    """ A corospoding profile is created when ever a user is created"""
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            id = 10,
        )


@receiver(post_delete,sender=Profile)
def deleteUser(sender, instance, **kwargs):
    """ A corosponding user is deleted whenever a profile is deleted """
    user = instance.user
    user.delete()