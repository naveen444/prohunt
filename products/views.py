from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Vote
from django.contrib import messages
from django.utils import timezone

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})

@login_required(login_url="/accounts/signup")
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
            return redirect('/products/' + str(product.id))
        else:
            messages.error(request, 'All fields are required !')
            return render(request, 'products/createp.html')
    else:
        return render(request, 'products/createp.html')

def detailp(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'products/detailp.html', {'product':product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk = product_id)
        if product.hunter.username == request.user.username:
            messages.error(request, "Creator can't upvote their own post !")
            return render(request, 'products/detailp.html', {'product':product})
        else:
            try:
                vote = Vote.objects.get(productID=product_id, userID=request.user)
                messages.error(request, 'You have already voted for this post!')
                return redirect('home')
            except Vote.DoesNotExist:
                vote = None
                # find product by id and increment
                product = Product.objects.get(id=product_id)
                vote = Vote(productID=product, userID=request.user)
                product.votes_total += 1
                vote.save()
                product.save()
                messages.success(request, 'upvoted successfully!')
                return redirect('home')

@login_required(login_url="/accounts/signup")
def user_created_posts(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    products = Product.objects.all()
    return render(request, 'products/userposts.html', {'products':products})


@login_required(login_url="/accounts/signup")
def deleteposts(request, user_id, product_id):
    product = get_object_or_404(Product, pk = product_id)
    if request.method == 'POST':
        user = get_object_or_404(User, pk = user_id)
        if user.check_password(request.POST['password']):
            product.delete()
            messages.success(request, 'post deleted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'password is incorrect !')
            return render(request,'products/deleteposts.html', {'product': product})
    else:
        return render(request,'products/deleteposts.html', {'product': product})
