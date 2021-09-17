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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = CityForm()
    #     if form.is_valid:
    #         form.save()
    #         context['form'] = form
    #     return context


class CityDetail(DetailView):
    model = City


class CityCreate(CreateView):
    template_name = 'cities/city_create.html'
    form_class = CityForm
    model = City


class CityUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'cities/city_update.html'
    form_class = CityForm
    model = City
    success_message = 'Город успешно отредактирован'


class CityDelete(DeleteView):
    model = City
    template_name = 'cities/city_delete.html'
    form_class = CityForm
    success_url = reverse_lazy('cities_list')

