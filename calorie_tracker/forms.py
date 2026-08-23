from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Food name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Calories'}),
        }