from django.urls import path
from .views import CitiesList, CityDetail, CityCreate, CityUpdate, CityDelete

urlpatterns = [
    path('', CitiesList.as_view(), name='home'),
    path('<int:pk>/', CityDetail.as_view(), name='detail'),
    path('create/', CityCreate.as_view(), name='create'),
    path('<int:pk>/update/', CityUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CityDelete.as_view(), name='delete'),

]