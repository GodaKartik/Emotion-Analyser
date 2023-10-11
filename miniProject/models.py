from django.db import models

# Create your models here.

class Thought(models.Model):
    thoughts = models.CharField(max_length=1000)
