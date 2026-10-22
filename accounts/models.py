from django.db import models
from django.utils import timezone
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
    
    def __str__(self):
        return self.user.Name
class JobApplicationTracker(models.Model):
    STATUS=[
        ("Applied","Applied"),
        ("Response","Response"),
        ("NoResponse","NoResponse"),
        ("Rejected","Rejected"),
        ("InterviewInProcess","InterviewInProcess")
    ]
    SALARYTYPE=[
        ("LPA","LPA"),
        ("MONTHLY","MONTHLY"),
        ("Not Disclosed","Not Disclosed")
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    CompanyName=models.CharField(max_length=50)
    JobRole=models.CharField(max_length=50)
    JobRequirement=models.TextField(max_length=250)
    SalaryPackage=models.DecimalField(max_digits=10,decimal_places=2)
    SalaryType=models.CharField(max_length=50,choices=SALARYTYPE)
    ApplicationDate=models.DateField(default=timezone.localdate)
    Status=models.CharField(max_length=50,choices=STATUS ,default="Applied")
    Bond=models.PositiveIntegerField(default=0)
    OriginalDocuments=models.BooleanField(default=False)
    JobURL=models.URLField(blank=True)
    