from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.random_quote, name='random_quote')
    ]