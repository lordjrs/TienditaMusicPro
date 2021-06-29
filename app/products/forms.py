from django import forms
from django.forms import ModelForm
from .models import Product

class PoleraForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image', 'excerpt', 'detail', 'price', 'available', 'category']