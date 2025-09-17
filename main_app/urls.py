from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('locations/', views.locations_index, name='location=index'),
    path('accounts/signup', views.signup, name='signup'),
]