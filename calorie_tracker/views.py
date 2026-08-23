from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    today = timezone.now().date()
    items = FoodItem.objects.filter(date_added=today)
    total = sum(item.calories for item in items)

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.date_added = today
            food.save()
            messages.success(request, f"Added {food.name} ({food.calories} kcal).")
            return redirect('calorie_tracker:index')
    else:
        form = FoodItemForm()

    return render(request, 'calorie_tracker/index.html', {
        'items': items,
        'total': total,
        'form': form,
        'today': today,
    })

def delete_item(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    messages.info(request, f"Removed {item.name}.")
    return redirect('calorie_tracker:index')

def reset_today(request):
    today = timezone.now().date()
    count, _ = FoodItem.objects.filter(date_added=today).delete()
    messages.warning(request, f"Reset today's entries ({count} items removed).")
    return redirect('calorie_tracker:index')