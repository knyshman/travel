from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import City


class CitiesList(ListView):
    model = City
    template_name = 'cities/home.html'


class CityDetail(DetailView):
    model = City
