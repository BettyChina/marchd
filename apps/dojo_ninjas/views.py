
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Item
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'dojo_ninjas/index.html')

def register(request):
    if User.userManager.isValidRegistration(request.POST, request):
        flag = True
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('index'))

def success(request):
    context = { "users": User.objects.all(), "items" : Item.objects.all()}

    return render(request, 'dojo_ninjas/success.html', context)

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        flag = True
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect (reverse('index'))

def create(request):
    if Item.itemManager.isValid(request.POST, request):
        flag = True
        
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('index'))