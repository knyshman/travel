from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TrainForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Train


class TrainsList(ListView):
    model = Train
    ordering = ['travel_time']
    paginate_by = 10
    template_name = 'trains/home.html'


class TrainDetail(DetailView):
    model = Train
    template_name = 'trains/train_detail.html'


class TrainCreate(LoginRequiredMixin, CreateView):
    template_name = 'trains/train_create.html'
    model = Train
    form_class = TrainForm
    success_message = 'Поезд успешно создан'
    success_url = reverse_lazy('trains:home')


class TrainUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'trains/train_update.html'
    model = Train
    success_message = 'Поезд успешно отредактирован'
    form_class = TrainForm
    success_url = reverse_lazy('trains:home')


class TrainDelete(LoginRequiredMixin, DeleteView):
    model = Train
    template_name = 'trains/train_delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален')
        return self.post(request, *args, **kwargs)
