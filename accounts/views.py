from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'username already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], email = request.POST.get('email'), password = request.POST['password'])
                user.first_name = request.POST.get('fname')
                user.last_name = request.POST.get('lname')
                user.profile.bio = request.POST.get('about')
                user.profile.image = request.FILES['pphoto']
                user.profile.birth_date = request.POST.get('dob')
                user.save()
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


def chgprofile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk = user_id)
        if user.check_password(request.POST['password']):
            user.username = request.POST.get('username')
            user.profile.bio = request.POST.get('about')
            if request.FILES['pphoto']:
                user.profile.image = request.FILES['pphoto']
            else:
                user.profile.image = user.profile.image
            user.save()
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/chgprofile.html', {'error': 'password didnt matched'})
        #user has info and wanna make account!
    else:
        #user wants to enter info
        return render(request,'accounts/chgprofile.html')
