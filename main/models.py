import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    date = models.DateTimeField('date published', default = timezone.now)

    def __str__(self):
        return self.postname