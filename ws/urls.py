from django.conf.urls import include, url
from django.contrib import admin
from ws import views

urlpatterns = [
    url(r'^sync/', views.sync),
]
