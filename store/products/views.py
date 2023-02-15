from django.shortcuts import render

def index(request):
   context = {
      'title': 'Store',
      'username': 'Aizhan Maratkyzy', 
   }
   return render(request, 'products/index.html', context)

def products(request):
   context = {
      'is_promotion': True,
   }
   return render(request, 'products/products.html', context)