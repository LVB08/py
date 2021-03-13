from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """披萨店的主页"""
    return render(request, 'pizzas/index.html')


def species(request):
    """显示所有的披萨"""
    species = Pizza.objects.order_by('date_added')
    context = {'species':species}
    return render(request, 'pizzas/species.html', context)


def ine(request,ine_id):
    """显示单个披萨及其所有配料"""
    ine = Pizza.objects.get(id=ine_id)
    toppings = ine.topping_set.order_by('-date_added')
    context ={'ine':ine,'toppings':toppings}
    return render(request, 'pizzas/ine.html', context)