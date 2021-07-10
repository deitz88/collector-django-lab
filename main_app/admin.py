from django.contrib import admin

# Register your models here.
from .models import Food, Mealtime, Ingredient
admin.site.register(Food)
admin.site.register(Mealtime)

admin.site.register(Ingredient)
