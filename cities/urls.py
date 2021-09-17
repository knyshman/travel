from django.urls import path
from .views import CitiesList, CityDetail, CityCreate, CityUpdate, CityDelete

urlpatterns = [
    path('', CitiesList.as_view(), name='cities_list'),
    path('<int:pk>/', CityDetail.as_view(), name='city_detail'),
    path('create/', CityCreate.as_view(), name='city_create'),
    path('<int:pk>/update/', CityUpdate.as_view(), name='city_update'),
    path('<int:pk>/delete/', CityDelete.as_view(), name='city_delete'),

]