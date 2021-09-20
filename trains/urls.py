from django.urls import path
from .views import *

urlpatterns = [
    path('', TrainsList.as_view(), name='home'),
    path('<int:pk>/', TrainDetail.as_view(), name='detail'),
    path('create/', TrainCreate.as_view(), name='create'),
    path('<int:pk>/update/', TrainUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', TrainDelete.as_view(), name='delete'),

    ]