from django.db import models
from django.contrib.auth.models import auth,User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phno = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

