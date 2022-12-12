from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    #path('',views.home, name='Home'), haci puedes agragar un url aparte debes crear un html
    path('',views.blog, name='Blog'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)