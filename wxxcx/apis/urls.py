from django.urls import path

from apis.views import weather

urlpatterns = [
    path('',weather,name='weather'),
]