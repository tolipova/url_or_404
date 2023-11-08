from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.html import mark_safe
# Register your models here. 
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category')

class PostsAdmin(admin.ModelAdmin):
    list_display = ('category','title','date','get_html_photo',)

    def get_html_photo(self,object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None
    get_html_photo.short_description = 'Surat'

admin.site.register(NavbarStart)
admin.site.register(Posts)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(Featured)
admin.site.register(MainSilder)
admin.site.register(StartSlider)
admin.site.register(Main_Popular)
admin.site.register(Popular)
admin.site.register(Main_Latest)
admin.site.register(Latest)
admin.site.register(Follow)
admin.site.register(NewsLetter)
admin.site.register(Addstart)
admin.site.register(Tranding)
admin.site.register(SingleNews)
admin.site.register(SingleComments)
admin.site.register(Users)



