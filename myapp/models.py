from django.db import models

# Create your models here.

class UserInfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

   

