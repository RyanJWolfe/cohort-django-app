from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
