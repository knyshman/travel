from django.contrib import admin
from .models import Train



class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = ('name', 'travel_time', 'from_city', 'to_city')
    list_editable = ('travel_time',)


admin.site.register(Train, TrainAdmin)