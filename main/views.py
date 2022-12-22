from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import *
from django.utils import timezone
from django.http import HttpResponse
from PIL import Image
# Create your views here.
def home(request):
    print(f"user is {request.user}")
    get_all_products = Product.objects.all()
    get_offered_products = Product.objects.filter(product_offer=True)
    if request.user.is_authenticated:
        get_cart_count = Cart.objects.filter(user = request.user).count()
        context = {
            'get_all_products': get_all_products,
            'get_offered_products': get_offered_products,
            'get_cart_count' : get_cart_count
        }
    else:
        context = {
            'get_all_products' : get_all_products,
            'get_offered_products' : get_offered_products
        }
    return render(request,'home.html',context)

def productview(request,id):
    get_clicked_product = Product.objects.filter(id = id)[0]
    get_reviews = Review.objects.filter(product = get_clicked_product)
    print("the image is ")
    # im = Image.open(get_clicked_product.product_image)
    # im.show()
    context = {

        'get_clicked_product':get_clicked_product,
        'get_reviews':get_reviews
    }
    # print(get_clicked_product.product_price)
    return render(request,'productview.html',context)

def cart(request):
    if request.method == "POST":
        hid = request.POST.get("hid","")

        if request.user.is_authenticated:
            if hid != "":
                user = request.user
                get_product = Product.objects.filter(id=hid).first()
                check_cart = Cart.objects.filter(user = request.user,product = get_product)
                if not check_cart:
                    create_cart = Cart.objects.create(user=user, product=get_product, quantity=1,price=get_product.product_price)
                    create_cart.save()

                get_added_product = Cart.objects.filter(user=request.user).order_by("added_time")
                if len(get_added_product) == 0:
                    return render(request, 'cart.html', {"get_added_product": get_added_product,'count':0})
                return render(request, 'cart.html', {"get_added_product": get_added_product,'count ': 1})
        if not request.user.is_authenticated:
            return render(request, 'login.html')
    get_added_product = Cart.objects.filter(user=request.user).order_by("added_time")
    if len(get_added_product) == 0:
        return render(request, 'cart.html', {"get_added_product": get_added_product, 'count': 0})
    return render(request, 'cart.html', {"get_added_product": get_added_product, 'count ': 1})

def update_cart(request,id):

    if request.method == "POST":
        qty = int(request.POST.get("qty","1"))

        if qty > 0:
            get_cart_product = Cart.objects.filter(id = id,user = request.user).first()
            price = get_cart_product.product.product_price * qty
            update = Cart.objects.filter(id = id,user = request.user).update(quantity = qty,price = price,added_time = timezone.now())
        return redirect("/cart/")

    elif id[-1] == 'r':
        new_id = id[:len(id) - 1]
        delete_cart_item = Cart.objects.filter(id = new_id).delete()
        return redirect("/cart/")