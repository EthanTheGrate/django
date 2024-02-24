from django.shortcuts import render
from .models import food

# Create your views here.
def index(request):
    food_details = food.objects.all()
    data = {
        "food_details" : food_details
    }
    return render("index.html", data)