'''
Created on 2014/10/17

@author: x-masashik
'''
from django.conf.urls import patterns, url, include
from milestones import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'diaries', views.DiaryViewSet)
router.register(r'milestones', views.MileStoneViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)