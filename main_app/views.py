from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Food, Mealtime, Ingredient
from .forms import MealtimeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',)

def assoc_ingredient(request, food_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Food.objects.get(id=food_id).ingredients.add(ingredient_id)
  return redirect('detail', food_id=food_id)

def about(request):
    return render(request, 'about.html',)
def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', {'foods': foods})
def foods_detail(request, food_id):
  food = Food.objects.get(id=food_id)
  ingredients_food_doesnt_have = Ingredient.objects.exclude(id__in = food.ingredients.all().values_list('id'))
  mealtime_form = MealtimeForm()
  return render(request, 'foods/detail.html', {
    'food': food, 'mealtime_form': mealtime_form,
    'ingredients' : ingredients_food_doesnt_have
  })
  

# CBV functions
class FoodCreate(CreateView):
	model = Food
	fields = '__all__'

class FoodUpdate(UpdateView):
	model = Food
	fields = '__all__'

class FoodDelete(DeleteView):
	model = Food
	success_url = '/foods/' 


# View functions

def add_mealtime(request, food_id):
    print('new_mealtime')
    # create a Model for instance using the data from request.POST
    form = MealtimeForm(request.POST)
    #custom validation
    if form.is_valid():
        new_mealtime = form.save(commit=False)
        new_mealtime.food_id = food_id
        new_mealtime.save()
    return redirect('detail', food_id=food_id)

