from django.urls import path
from . import views

urlpatterns = [
    path('get/<str:url>/', views.getUrl, name="get-url"),
    path('add/', views.addUrl, name="add-url"),
]