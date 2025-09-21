from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Location, Review
from .forms import ReviewForm

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', { 'form': form, 'error_message': error_message })

@login_required
def locations_index(request):
    locations = Location.objects.all()

    return render(request, 'locations/index.html', { 'locations': locations })

@login_required
def location_detail(request, location_id):
    location = Location.objects.get(id=location_id)

    reviewed = Review.objects.filter(location=location, user=request.user).exists()

    return render(request, 'locations/detail.html', { 'location': location, 'reviewed': reviewed })

class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'city', 'tag', 'image', 'description', 'birds']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['tag', 'image', 'description', 'birds']

class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = '/locations/'

@login_required
def review_index(request):
    reviews = Review.objects.filter(user=request.user)

    return render(request, 'main_app/my_reviews.html', { 'reviews': reviews })

@login_required
def create_review(request, location_id):
    location = Location.objects.get(id=location_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            review.location = location
            review.user = request.user

            review.save()

            return redirect('location-detail', location_id=location_id)
    else:
        form = ReviewForm()

    return render(request, 'main_app/review_form.html', { 'form': form, 'location': location })

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['title', 'rating', 'date', 'text']
    
class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    
    def get_success_url(self):
        location_id = self.object.location.id
        return reverse_lazy('location-detail', kwargs={ 'location_id': location_id })

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['location'] = self.object.location
            return context

