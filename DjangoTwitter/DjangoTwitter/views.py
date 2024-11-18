from django.shortcuts import render,redirect
from twitter.models import Tweet
from twitter.forms import UserRegistrationForm
from django.contrib.auth import login

def Home(request):    
    if request.method == 'POST':
        prefix = request.POST['search']
        print(prefix)
        tweets = Tweet.objects.filter(title__contains=prefix) or Tweet.objects.filter(description__contains=prefix)
        print(tweets)
    else:
        tweets = Tweet.objects.all()
    return render(request,'index.html',{'tweets':tweets})

   