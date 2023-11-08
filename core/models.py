from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
class MainCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_info/')

class MainSilder(models.Model):
    image = models.ImageField(upload_to='user_info/')
    date = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class StartSlider(models.Model):
    image = models.ImageField(upload_to='user_info/')
    info = models.CharField(max_length=255)

class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='user_info/')
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Featured(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    info = models.TextField()

    def __str__(self):
        return self.title
    
class Main_Popular(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)
    little_info = models.CharField(max_length=255)
    big_info = models.TextField()

    def __str__(self):
        return self.title
class Popular(models.Model):
    image = models.ImageField(upload_to='user_info/')    
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

class Main_Latest(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)
    little_info = models.CharField(max_length=255)
    big_info = models.TextField()

        
class Latest(models.Model):
    image = models.ImageField(upload_to='user_info/')    
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

class Follow(models.Model):
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    you_tube = models.CharField(max_length=255)
    vimeo = models.CharField(max_length=255)

class NewsLetter(models.Model):
    info = models.TextField()
    button = models.CharField(max_length=255)
    small_info = models.CharField(max_length=255)

class Addstart(models.Model):
    image = models.ImageField(upload_to='user_info/') 

class Tranding(models.Model):
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False)   
    info = models.CharField(max_length=255)

class NavbarStart(models.Model):
    home  = models.CharField(max_length=255)
    categories  = models.CharField(max_length=255)
    # singlenews  = models.CharField(max_length=255)
    dropdown  = models.CharField(max_length=255)
    item1 = models.CharField(max_length=255)
    item2 = models.CharField(max_length=255)
    item3 = models.CharField(max_length=255)
    contact  = models.CharField(max_length=255)

class SingleNews(models.Model):
    singlenews  = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_info/')
    date = models.DateField(auto_now=False)
    header = models.CharField(max_length=255)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    header2 = models.CharField(max_length=255)
    hed2_img =  models.ImageField(upload_to='user_info/')
    hed2_paragraph = models.TextField()
    header3 = models.CharField(max_length=255)
    hed3_img =  models.ImageField(upload_to='user_info/')
    hed3_paragraph = models.TextField()

    

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})


    
    
class SingleComments(models.Model):
    image = models.ImageField(upload_to='user_info/')
    user_name = models.CharField(max_length=255)
    comment = models.TextField()
    button = models.CharField(max_length=255)


    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id':self.pk})


       
class Users(models.Model):
    user_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    work_place = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False , unique=True)

    def __str__(self):
        return self.user_name