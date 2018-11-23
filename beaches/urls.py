from django.conf.urls import patterns, url
from beaches import views

urlpatterns = patterns('',
        url(r'^$',views.index, name='index'),
        url(r'^index/',views.index, name='index'),
        url(r'^add_category/',views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'))
