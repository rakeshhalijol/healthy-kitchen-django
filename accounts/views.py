from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import Profile
# Create your views here.
def signin(request):
    if request.method == "POST":
        sname = request.POST.get("sname","")
        semail = request.POST.get("semail","")
        sphone = request.POST.get("sphone","")
        spass1 = request.POST.get("spass1","")
        spass2 = request.POST.get("spass2","")
        print(sname)
        print(semail)
        print(sphone)
        print(spass1)
        print(spass2)

        if sname == "" or semail == "" or sphone == "" or spass1 == "" or spass2 == "":
            messages.error(request,"All credentials are required")
            return redirect("/accounts/signin/")

        get_name = User.objects.filter(username = sname)
        if len(get_name) != 0:
            messages.error(request,"Username Already exists")
            return redirect('/accounts/signin/')
        get_email = User.objects.filter(email = semail)
        if len(get_email) != 0:
            messages.error(request,"Email Already exists")
            return redirect('/accounts/signin/')
        if spass1 != spass2:
            messages.error(request,"Password Missmatch")
            return redirect('/accounts/signin/')
        if len(spass1) < 4 or len(spass2) < 4:
            messages.error(request,"Length of password should be atleast 4")
            return redirect('/accounts/signin/')

        create_user = User.objects.create_user(username = sname,email = semail,password = spass1).save()
        user = auth.authenticate(username=sname, password=spass1)
        auth.login(request,user)
        return redirect("/")

    return render(request,'signin.html')

def login(request):
    if request.method == "POST":
        lname = request.POST.get("lname","")
        lpass = request.POST.get("lpass","")

        if lname == "" or lpass == "":
            messages.error(request,"All credentials are required")
            return redirect("/accounts/login/")
        user = auth.authenticate(username=lname, password=lpass)
        if user:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("/accounts/login/")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")



