from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "auth/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "auth/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            fname = user.first_name
            return render(request, "auth/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "auth/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
