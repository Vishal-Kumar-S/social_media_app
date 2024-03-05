from django.db import models

class profiles(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=60)
    bio = models.TextField()
    last_active = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name