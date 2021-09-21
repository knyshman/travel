from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import CityForm
from .models import City


class CitiesList(ListView):
    model = City
    template_name = 'cities/home.html'
    paginate_by = 10


class CityDetail(DetailView):
    model = City
    template_name = 'cities/city_detail.html'


class CityCreate(LoginRequiredMixin, CreateView):
    template_name = 'cities/city_create.html'
    form_class = CityForm
    model = City
    success_url = reverse_lazy('cities:home')


class CityUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'cities/city_update.html'
    form_class = CityForm
    model = City
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно отредактирован'


class CityDelete(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'cities/city_delete.html'
    form_class = CityForm
    success_url = reverse_lazy('cities:home')

