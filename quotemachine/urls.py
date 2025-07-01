from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_quote, name='add_quote'),
    path('like/<int:quote_id>/', views.like_quote, name='like_quote'),
    path('dislike/<int:quote_id>/', views.dislike_quote, name='dislike_quote'),
    path('', views.random_quote, name='random_quote')
]