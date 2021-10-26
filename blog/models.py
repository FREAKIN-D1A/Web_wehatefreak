from django.db import models
from django.utils import timezone
from django.utils.dateformat import format
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Post(models.Model):
    
    post_id = models.AutoField(primary_key=True)
    date_posted = models.DateField()
    time_posted = models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "Post is: {} by {}".format(self.post_id, self.author.username)

