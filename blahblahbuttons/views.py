from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def index(request):
    return render_to_response('blahblahbuttons/index.html')

def shop(request):
    return render_to_response('myshop/shop.html')

def cart(request):
    return render_to_response('myshop/cart.html')

def product(request):
    return render_to_response('myshop/products.html')

def product_detail(request):
    return render_to_response('myshop/product_detail.html')