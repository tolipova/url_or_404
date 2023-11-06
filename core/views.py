from django.shortcuts import render , get_object_or_404
from .models import *
# Create your views here.
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
    context ={
        'post':post,
        'cat_selected':post_id
    }
    return render(request, 'single.html', context=context)

# def show_post(request, post_id):
#     post = get_object_or_404(SingleComments, pk=post_id)
#     context ={
#         'post':post,
#         'cat_selected':post_id
#     }
#     return render(request, 'single.html', context=context)