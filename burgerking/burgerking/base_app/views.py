from django.shortcuts import render
from django.http import HttpResponse
from base_app.models import ItemList,Items,AboutAs,BookTable
# Create your views here.

def HomeView(request):
    items=Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'home.html', {'items':items,'list':list})

def AboutView(request):
    data =AboutAs.objects.all()
    return render(request,'about.html',{'data':data})


def MenuView(request):
    items=Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html', {'items':items,'list':list})


def BookTableView(request):
    return render(request,'book_table.html')


