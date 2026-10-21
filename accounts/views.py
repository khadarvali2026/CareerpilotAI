from django.shortcuts import render,HttpResponse,redirect
from accounts.models import User,UserProfile
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def signup(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        PhoneNumber=request.POST.get("PhoneNumber")
        Gender=request.POST.get("Gender")
        Password=request.POST.get("Password")
        #checking all are filled or not 
        if not all([Name, Email, PhoneNumber, Gender, Password]):
            return HttpResponse("All fields are required")
        #checking the Email or NUmber already Exists or not
        if User.objects.filter(Email=Email).exists():
            return HttpResponse("Email is Already Existed")
        if User.objects.filter(PhoneNumber=PhoneNumber).exists():
            return HttpResponse("Phone Number is Already Exists")

        User.objects.create(
            Name=Name,
            Email=Email,
            PhoneNumber=PhoneNumber,
            Gender=Gender,
            Password=make_password(Password)
            )
        return redirect("loginlink")
    return render(request,"accounts/signup.html")
def login(request):
    if request.method=="POST":
        EmailOrPhone=request.POST.get("EmailOrPhone")
        Password=request.POST.get("Password")
        try:
            if EmailOrPhone.isdigit():
                user=User.objects.get(
                    PhoneNumber=int(EmailOrPhone)
                    )
            else:
                user=User.objects.get(Email=EmailOrPhone)
                
            if check_password(Password,user.Password):
                request.session.cycle_key()
                request.session["USER ID"]=user.id
                request.session["Email"]=user.Email
                request.session["Name"]=user.Name
                return render(request,"accounts/dashboard.html")
            else:
                return HttpResponse("Invalid Creditionals")
        except User.DoesNotExist:
            return HttpResponse("First Register")
        except User.MultipleObjectsReturned:
            return HttpResponse("Multiple Accounts Registered") 
    
    return render(request,"accounts/login.html")