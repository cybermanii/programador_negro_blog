"""programadorNegroBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from programadorNegroBlog.views import index, pythonPagina, javascriptPagina, tutorialesPagina, capitulosPagina, contacto, argumentos, validacion, data, loginView, tecnologias, loadFile

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='inicio'),
    path('', loginView),
    path('login/', loginView),
    
    path('tecnologias/', tecnologias, name='tecnologias'),
    path('pythonp/', pythonPagina, name='python'),
    path('javascriptp/', javascriptPagina, name='javascript'),
    path('tutorialesp/', tutorialesPagina, name='tutoriales'),
    path('capitulosp/', capitulosPagina, name='capitulos'),

    path('productos/', loadFile, name='loadfile'),

    path('argumentos/', argumentos),
    path('validacion/<str:name>/<int:edad>',validacion),
    path('data/',data),

    path('contactame/',contacto, name='contacto'),
    path('api/', include('api_blog.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

