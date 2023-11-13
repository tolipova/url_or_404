from django.shortcuts import render , get_object_or_404, redirect
from .models import * 
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            form.save()
            user = authenticate(username=username, password=password)
            login(request, form)
            return redirect('home')
    else:
         form = UserCreationForm()
    return render (request, 'registration/register.html', {'form':form})           
     



@login_required
def info(request):
    navbar = NavbarStart.objects.all()
    category = Category.objects.all()
    main_category = MainCategory.objects.all()
    posts = Posts.objects.all()
    feature = Featured.objects.all()
    silder = MainSilder.objects.all()
    starts = StartSlider.objects.all()
    popular = Main_Popular.objects.all()
    second_popular = Popular.objects.all()
    latest = Main_Latest.objects.all()
    latest_info = Latest.objects.all()
    follow = Follow.objects.all()
    newsletter = NewsLetter.objects.all()
    addstart = Addstart.objects.all()
    tranding = Tranding.objects.all()
    singlenews = SingleNews.objects.all()
    comments = SingleComments.objects.all()
    context = {
        'navbar':navbar,
        'main_category':main_category,
        'category':category,
        'posts':posts,
        'feature':feature,
        'silder':silder,
        'starts':starts,
        'popular':popular,
        'second_popular':second_popular,
        'latest':latest,
        'latest_info':latest_info,
        'follow':follow,
        'newsletter':newsletter,
        'addstart':addstart,
        'tranding':tranding,
        'singlenews':singlenews,
        'comments':comments
    }
    return render (request, 'index.html', context)



def show_post(request, post_id):
    post = get_object_or_404(SingleNews, pk=post_id)
    comment = SingleComments.objects.all()
    context ={
        'post':post,
    }
    return render(request, 'single.html', context=context)

def add_user(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
            # return HttpResponse(f"Malumot xato yuborildi ")    
            form = UserForms()
    context = {
            'form':form
        }
    return render(request, 'forms.html', context )

def add_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
            # return HttpResponse(f"Malumot xato yuborildi ")    
            form = PostForms()
    context = {
            'form':form
        }
    return render(request, 'post_form.html', context )