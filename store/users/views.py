from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render
from .forms import *



# def login(req):
#    return render(req,'login.html')

# def register(req):
#    return render(req,'register.html')
def login(request):
   if request.method == 'POST':
      form = UserLoginForm(data = request.POST)
      if form.is_valid():
         username = request.POST['username']
         password = request.POST['password']
         user = AUTHENTICATION.authenticate(username=username, password=password)
         if user:
            AuthenticationError.login(request, user)
            return HttpResponseRedirect(reverse('store:product'))
   else:
      form = UserLoginForm()
   context = {'form': form}
   return render(request, 'users/login.html', context)

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(data = request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('users:login'))
   else: 
      form = UserRegisterForm()
   context = {'form': form}
   return render(request, 'users/register.html',context)