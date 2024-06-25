from django.shortcuts import render


# Create your views here.

def category_view(request):
    return render(request, 'product/category.html')


def product_details_view(request):
    return render(request, 'product/product_details.html')


def checkout_view(request):
    return render(request, 'product/checkout.html')

def cart_view(request):
    return render(request ,'product/cart.html')

def blog_view (request):
    return render(request ,'blog/blog.html')

def blog_details_view (request):
    return render(request ,'blog/blog_details.html')

def tracking_view (request):
    return render(request,'pages/tracking.html')

def elements_view(request):
    return render(request, 'pages/elements.html')

def contact_view(request):
    return render(request, 'contact/contact.html')