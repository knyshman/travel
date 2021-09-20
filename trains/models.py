from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    travel_time = models.PositiveSmallIntegerField(verbose_name="Время в пути")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город отправления', related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город прибытия', related_name='to_city')

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city} в город {self.to_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Измените город прибытия')

        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk})
