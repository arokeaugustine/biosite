from django.urls import path
from . import views


urlpatterns = [
    path('', views.collection, name='collection'),
    path('<slug:slug>', views.specimenspage, name='specimen'),
]
