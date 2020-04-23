from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                messages.error(request, 'Username already exist!')
                return render(request,'accounts/signup.html')
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
            messages.error(request, 'Passwords did not matched!')
            return render(request,'accounts/signup.html')
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
            messages.error(request, 'invalid username or password!')
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you have successfully logged out.')
        return redirect('home')


def chgprofile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk = user_id)
        if user.check_password(request.POST['password']):
            try:
                if user.username != request.POST.get('username'):
                    user = User.objects.get(username = request.POST.get('username'))
                    messages.error(request, 'Username already exist!')
                    return render(request,'accounts/chgprofile.html')
                else:
                    pass
            except User.DoesNotExist:
                pass
            user.username = request.POST.get('username')
            try:
                if user.email != request.POST.get('email'):
                    user = User.objects.get(email = request.POST.get('email'))
                    messages.error(request, 'account with this email already exist!')
                    return render(request,'accounts/chgprofile.html')
                else:
                    pass
            except User.DoesNotExist:
                pass
            user.email = request.POST.get('email')
            user.profile.bio = request.POST.get('about')
            try:
                user.profile.image = request.FILES['photo']
            except KeyError:
                pass
                # user.profile.image = user.profile.image
            user.save()
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Old password did not matched!')
            return render(request,'accounts/chgprofile.html')
        #user has info and wanna make account!
    else:
        #user wants to enter info
        return render(request,'accounts/chgprofile.html')

def chgpassword(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk = user_id)
        if user.check_password(request.POST['oldpassword']):
            user.set_password(request.POST['newpassword'])
            user.save()
            auth.logout(request)
            return render(request,'accounts/login.html')
        else:
            messages.error(request, 'password didnt matched!')
            return render(request,'accounts/chgpassword.html')
    else:
        return render(request,'accounts/chgpassword.html')
