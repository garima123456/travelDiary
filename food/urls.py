from django.conf.urls import patterns, url
from food import views

urlpatterns = patterns('',
        url(r'^$',views.index2, name='index2'),
        url(r'^index2/',views.index2, name='index2'),
           )
