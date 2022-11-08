from os import remove
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse

from .forms import CreateUserForm, ProfileUpdateForm
from .models import Profile

# Create your views here. 

def home(request):
    return HttpResponse("Hello")

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context={
        'form': form,
    }
    return render(request, 'accounts/signup.html',context)

def profile_view(request,pk):
    profile = get_object_or_404(Profile, pk=pk)
    
    #Get all profiles following the above user's profile
    followers = profile.followers.all()
    num_followers=len(followers)
    #Get all profiles followed by the above user's profile
    following=profile.user.followers.all()
    num_following = len(following)
    
    
    posts=profile.user.posts.all()

            
    context = {
        'profile':profile,
        'followers':followers,
        'num_followers':num_followers,
        'num_following':num_following,
 
        'posts':posts,
        
    }
    return render(request, 'accounts/profile.html',context)

def profile_update(request,pk):
    profile = Profile.objects.get(pk=pk)
    
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile',pk)
    else:
        p_form = ProfileUpdateForm(instance=profile)
    context ={
        'p_form': p_form,
    }
    return render(request, 'accounts/profile_update.html',context)



        
def follow(request,pk):
    profile = Profile.objects.get(pk=pk)
    followers = profile.followers.all()
    
    #Get all profiles followed by the above user's profile
    following=profile.user.followers.all()
    num_following = len(following)
   
    if request.user not in profile.followers.all():
        profile.followers.add(request.user)
    else:
        profile.followers.remove(request.user)
        
    num_followers=len(followers)
    context ={
        'profile': profile,
        'followers':followers,
        'num_followers':num_followers,
        'num_following':num_following,
        }
    return render(request, 'partials/follow.html',context)