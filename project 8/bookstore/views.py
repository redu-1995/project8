from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
   info = BookInformation.objects.all()
   book = Book.objects.all()
   
   data ={
      
      'info':info,
      'books':book
   }
   
   return render(request, 'home.html',data)

def about(request):
   return render(request, 'about.html')

def contact_us(request):
   return render(request,'contact.html')

def book(request):
     book = Book.objects.all()
     category = Category.objects.all()
   
     data ={
      
      'books':book,
      'categorys':category
   }
   
     return render(request, 'book.html',data)