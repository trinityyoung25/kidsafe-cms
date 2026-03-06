from django.db import models
from django.contrib.auth.models import User

class ChildProfile(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    age_category = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ActivityLog(models.Model):
    child = models.ForeignKey(ChildProfile, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    access_time = models.DateTimeField(auto_now_add=True)
