from django.contrib import admin
from blog_app.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    '''fieldsets = [
                ('Content', {"fields" : ["title"]}),
                ('Nickname Group', {"fields" : ["nickName"]})
                ]'''
    #fields = ["nickName","message"]

admin.site.register(Blog,BlogAdmin)