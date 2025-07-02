from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_quote, name='add_quote'),
    path('like/<int:quote_id>/', views.like_quote, name='like_quote'),
    path('dislike/<int:quote_id>/', views.dislike_quote, name='dislike_quote'),
    path('top/', views.top_quotes, name='top_quotes'),
    path('edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('', views.random_quote, name='random_quote')
]