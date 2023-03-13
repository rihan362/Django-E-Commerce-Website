from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Products
from .models import Contact


# Create your views here.
def index(request):
    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)
    
    # products=Products.objects.all()
    # print(products)
    # n=len(products)
    # nSlides=n//4+ceil((n/4)+(n//4))
    # # params={'no_ofslides': nSlides,'range':range(1,nSlides),'product':products}
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    # params={'allProds':allProds }
    return render(request,'shop/index.html',params)
    
    
    
def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request,myid):
    product=Products.objects.filter(id=myid)
    print(product)
    return render(request,'shop/products.html', {'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')
