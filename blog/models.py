from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title

class Cv(models.Model):
    
    name = models.CharField(max_length=50, default='None')
    address = models.TextField(default='None')
    telephone = models.CharField(max_length=15, default='None')
    mobile = models.CharField(max_length=15, default='None')
    email = models.CharField(max_length=50, default='None')
    summary = models.TextField(default='None')
    skills = models.TextField(default='None')
    education = models.TextField(default='None')
    work = models.TextField(default='None')
    voluntary = models.TextField(default='None')
    interests = models.TextField(default='None')
    referees = models.TextField(default='None')

    def __str__(self):
        return self.name
        