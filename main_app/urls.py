from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('locations/', views.locations_index, name='location-index'),
    path('locations/<int:location_id>', views.location_detail, name='location-detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='location-create'),
    path('locations/<int:pk>/update', views.LocationUpdate.as_view(), name='location-update'),
    path('locations/<int:pk>/delete', views.LocationDelete.as_view(), name='location-delete'),
    path('reviews/', views.review_index, name='review-index'),
    path('reviews/create/<int:location_id>', views.create_review, name='create-review'),
    path('reviews/update/<int:location_id>/<int:pk>', views.ReviewUpdate.as_view(), name='update-review'),
    path('reviews/delete/<int:location_id>/<int:pk>', views.ReviewDelete.as_view(), name='delete-review'),
    path('accounts/signup', views.signup, name='signup'),
]