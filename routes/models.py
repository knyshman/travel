from django.db import models
from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, verbose_name='Маршрут', unique=True)
    travel_times = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город отправления', related_name='route_from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город прибытия', related_name='route_to_city')
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут {self.name} из города {self.from_city} в город {self.to_city}'

    class Meta:
        verbose_name = 'Маршруты'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']



