from django.db import models
from django.db.models.fields import DateField

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  amount = models.IntegerField()

class Food(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    ingredients = models.ManyToManyField(Ingredient)


class Mealtime(models.Model):
    date = models.DateField('meal date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
  )
    
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    

    
    
    