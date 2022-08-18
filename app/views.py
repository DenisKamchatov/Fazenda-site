from app.models import Contacts, Cottage, Gallery, Photogallery
from django.shortcuts import render


def site(request):
    cottage = Cottage.objects.all()
    gallery = Gallery.objects.all()
    contacts = Contacts.objects.all()
    context = {
        "cottage": cottage,
        "gallery": gallery,
        "contacts": contacts,       
    }
    return render(request, 'app/index.html', context=context)


def photogallery(request):
    photogallery = Photogallery.objects.all()
    contacts = Contacts.objects.all()
    context = {
        "photogallery": photogallery,
        "contacts": contacts, 
    }
    return render(request, 'app/gallery.html', context=context)
