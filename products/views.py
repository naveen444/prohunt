from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    return render(request, 'products/home.html')

@login_required
def createp(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST['p_descrpt'] and request.POST['p_summary'] and request.POST['url'] and request.FILES['Icon'] and request.FILES['Image']:
            product = Product()
            product.title = request.POST.get('title')
            product.product_description = request.POST['p_descrpt']
            product.product_summary = request.POST['p_summary']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['Icon']
            product.image = request.FILES['Image']

            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/createp.html',{'error':'All fields are required'})
    else:
        return render(request, 'products/createp.html')
