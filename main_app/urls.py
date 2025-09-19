from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('locations/', views.locations_index, name='location-index'),
    path('locations/<int:location_id>', views.location_detail, name="location-detail"),
    path('locations/create/', views.LocationCreate.as_view(), name='location-create'),
    path('accounts/signup', views.signup, name='signup'),
]