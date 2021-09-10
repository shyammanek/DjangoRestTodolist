from django.db import models
from rest_framework import serializers


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=500,null=True)
    detail = models.CharField(max_length=500,null=True)
    completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title