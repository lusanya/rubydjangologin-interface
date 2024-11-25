from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    login_time=models.DateTimeField (auto_now_add=True) #adding time
    def __str__(self):
        return f"({self.username} log in at {self.login_time})"

class Reset (models.Model):
    username=models.CharField (max_length=10)
    password=models.CharField (max_length=10)
    def __str__(self):
        return self.username,self.password


class Register(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

