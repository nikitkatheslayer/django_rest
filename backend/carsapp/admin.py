from django.contrib import admin

import carsapp.models as model

admin.site.register(model.Car)
admin.site.register(model.HistoryCar)
admin.site.register(model.DetailCar)
