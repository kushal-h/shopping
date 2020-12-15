import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from main.models import products

def product() :

    p1 = products()
    p1.name = 'kushal'
    p1.img = 'cloth_1.jpg'
    p1.desc = 'nice top'
    p1.price = 545

    p2 = products()
    p2.name = 'Corater'
    p2.img = 'shoe_1.jpg'
    p2.desc = 'Finding perfect products'
    p2.price = 50

    p3 = products()
    p3.name = 'Polo Shirt'
    p3.img = 'cloth_2.jpg'
    p3.desc = 'Finding perfect products'
    p3.price = 50

    p4 = products()
    p4.name = 'T-Shirt Mockup'
    p4.img = 'cloth_3.jpg'
    p4.desc = 'Finding perfect products'
    p4.price = 50

    prods = [p1, p2, p3, p4 ]
    return prods

def Main(request):

    prods = product()

    return render(request, 'index.html' , {'prods' : prods})

def sell(request):
    if request.method == 'post':
        pname = request.post['pname']
        price = request.post['price']
        des = request.post['des']
        try:
            folder = 'media/images/'
            uploaded_image = request.FILES['prod']
            print("Name is:", uploaded_image.name)

            # if not uploaded_image:
            # return Response({"error": "Choose file"}, status=status.HTTP_400_BAD_REQUEST)
            # for f in myfiles:
            filename = str(uploaded_image.name)
            fs = FileSystemStorage(location=folder)  # defaults to DATASTORE
            name = fs.save(uploaded_image.name, uploaded_image)
            mediapath = folder + "{}"
            filepath = os.path.join(mediapath).format(name)
            print(filepath)
            product = selling()
            product.price = price
            product.product_name = pname
            product.product_image = filepath
            product.save()

        except Exception as e:
            print("errors is :", e)
        return HttpResponseRedirect(reverse('main'))
    else:

        return render(request, 'sell.html')

