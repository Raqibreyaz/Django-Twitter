from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('add/',views.add_tweet,name='add'),
    path('read/<int:id>/',views.read_tweet,name='read'),
    path('update/<int:id>/',views.update_tweet,name='update'),
    path('delete/<int:id>/',views.delete_tweet,name='delete'),
]