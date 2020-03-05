from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'username already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error': 'password didnt matched'})
        #user has info and wanna make account!
    else:
        #user wants to enter info
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'user not found!'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
