from django.urls import path
from .views import CitiesList, CityDetail

urlpatterns = [
    path('', CitiesList.as_view(), name='cities_list'),
    path('<int:pk>/', CityDetail.as_view(), name='city_detail')
]