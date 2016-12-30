from django.db import models
import datetime


class Story(models.Model):

    content = models.CharField(max_length=2048)
    type = models.IntegerField(default=1)
    is_valid = models.BooleanField(default=True)
    create_time = models.DateField(default=datetime.datetime.now)
