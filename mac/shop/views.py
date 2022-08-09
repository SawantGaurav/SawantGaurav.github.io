from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from . models import Product



# Create your views here.

def index(request):
    return render(request ,'shop/index.html')
    
    # product = Product.objects.all()
    
    # context={'product':product}
    
    # return render(request, "shop/index.html",context)

def about(request):
    return render(request ,'shop/about.html')

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productView(request):
    return HttpResponse("we are at product View")

def checkout(request):
    return HttpResponse("we are at checkout")






