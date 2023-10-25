from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


Status = (('Read', 'Read'), ('Unread', 'Unread'))

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject", max_length=100)
    message = models.TextField(verbose_name="Message")
    status = models.CharField(verbose_name="Status", max_length=100, null=True, choices=Status, default="Unread")

    def __str__(self):
        return f'{self.name}'


class Notification(models.Model):
        
    class Meta:
        verbose_name_plural = 'Notifications'
        verbose_name = 'Notification'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")


class WebsiteContent(models.Model):
        
    class Meta:
        verbose_name_plural = 'WebsiteContents'
        verbose_name = 'WebsiteContent'

    name = models.CharField(verbose_name="Name", max_length=100)
    phoneNumber = models.CharField(verbose_name="Phone Number", max_length=100)
    emailAddress = models.EmailField(verbose_name="Email Address")
    address = models.CharField(verbose_name="Physical Address", max_length=100, default="None")
    websiteURL = models.CharField(verbose_name="Website URL", max_length=200, default="#")

    def __str__(self):
        return f'{self.name}'