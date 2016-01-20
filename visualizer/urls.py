from django.conf.urls import patterns, url

from visualizer import views

urlpatterns = patterns('', url(r'^$', views.index, name='historical'))
