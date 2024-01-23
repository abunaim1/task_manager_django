from django.shortcuts import render, redirect
from category.forms import CategoryForm
# Create your views here.

def category(request):
    if request.method == 'POST':
        data = CategoryForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('category')
    
    else:
        data = CategoryForm()
    return render(request, 'category.html', {'form':data})