from django.contrib import admin

from apps.cars.models import Car, CarImage

# Register your models here.
class CarImageAdminTabularInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarInStockAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
    inlines = [CarImageAdminTabularInline]

@admin.register(CarImage)
class CarInStockImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')