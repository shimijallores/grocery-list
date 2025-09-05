from django.shortcuts import render, redirect
from .forms import GroceryForm
from .models import GroceryItem

def grocery_list(request):
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grocery_list')
    else:
        form = GroceryForm()

    items = GroceryItem.objects.all()
    return render(request, 'grocery/index.html', {'form': form, 'items': items})
