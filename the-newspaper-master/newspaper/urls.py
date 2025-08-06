from django.urls import path
from newspaper import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
]