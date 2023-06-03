from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


@login_required(login_url='signin')
def mainPage(request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        
        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                # Log use in and redirect to settings page
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                # Create a profile object for new users created
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                messages.info(request, 'Success!')
                return redirect('settings')
        else: 
            messages.info(request, 'Passwords Do Not Match!')
            return redirect('signup')
    else:
        context = {
            
        }
        return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Credentials are wrong')
            return redirect('signin')
        
    return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
                
    
    context = {
        'user_profile':  user_profile,
        
    }
    return render(request, 'settings.html', context)