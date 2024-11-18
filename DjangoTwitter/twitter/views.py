from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm

def read_tweet(request,id):
    tweet_details = get_object_or_404(Tweet,pk=id)
    return render(request,'twitter/read_tweet.html',{'tweet_details':tweet_details})

@login_required
def add_tweet(request):
    if request.method == 'POST':
       form = TweetForm(request.POST,request.FILES)
       if form.is_valid():
          tweet=form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('home')
    else: 
        form = TweetForm()
    return render(request,'twitter/add_tweet.html',{'form':form})

@login_required
def update_tweet(request,id):
    tweet = get_object_or_404(Tweet,pk=id,user=request.user)
    if request.method=='POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            # tweet.user = request.user
            tweet.save()
            print('updatd tweet',tweet)
            return redirect('home')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'twitter/update_tweet.html',{'form':form})

@login_required
def delete_tweet(request,id):
  tweet = get_object_or_404(Tweet,pk=id,user=request.user)
  if request.method =='POST':
      tweet.delete()
      return redirect('home')
  return render(request,'twitter/delete_tweet.html')

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('home')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})