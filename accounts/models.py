from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=50)
    PhoneNumber=models.CharField(max_length=10,unique=True)
    Password=models.CharField(max_length=150)
    Status=models.BooleanField(default=True)
    Email=models.EmailField(unique=True)
    Gender=models.CharField(max_length=50)

    
    def __str__(self):
        return self.Name
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Education=models.CharField(max_length=50)
    PassedOut=models.PositiveIntegerField()
    Bio=models.TextField(max_length=250)
    College=models.CharField(max_length=50)
    Skills=models.TextField(max_length=200)
    
    