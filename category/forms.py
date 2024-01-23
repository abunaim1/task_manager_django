from django import forms
from category.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'assignDate' : forms.DateInput(attrs={'type' : 'datetime-local'})
        }