from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('title','image','description')

admin.site.register(Tweet,TweetAdmin)
