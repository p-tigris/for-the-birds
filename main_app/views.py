from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Location

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

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

def locations_index(request):
    locations = Location.objects.all()

    return render(request, 'locations/index.html', { 'locations': locations })

def location_detail(request, location_id):
    location = Location.objects.get(id=location_id)

    return render(request, 'locations/detail.html', { 'location': location })

class LocationCreate(CreateView):
    model = Location
    fields = ['name', 'city', 'tag', 'description', 'birds']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
