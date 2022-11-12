from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.postlist, name='post'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
