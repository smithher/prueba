from django.shortcuts import render,HttpResponse
from blog.models import Post, Categoria 

#def home(request):
   # return render(request, "ProyectoWebApp/home.html")

def blog(request):
    posts=Post.objects.all()
    return render (request, "ProyectoWebApp/index.html",{"posts":posts})

