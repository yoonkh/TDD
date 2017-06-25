from django.shortcuts import render, redirect
from .models import Item, List


def home_page(request):
    if request.method == 'POST':
        return render(request, 'home.html')

    items = Item.objects.all()
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

