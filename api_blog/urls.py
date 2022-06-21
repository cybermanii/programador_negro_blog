# # PASO 10
# # se importan las siguientes clases
# from django.contrib import admin
# from django.urls import path
# from .viewsets import ComputadoraViewSet, MarcaViewSet, ProcesadorViewSet, ramViewSet, DiscoViewSet, MarcaProcesadorViewSet
# from rest_framework import routers

# # se establece la funcion SimpleRouter() en una variable
# route = routers.SimpleRouter()

# # establece el path final
# # ejemplo localhost/api/Computadora
# route.register('computadora',ComputadoraViewSet)
# route.register('marca',MarcaViewSet)
# route.register('procesador', ProcesadorViewSet)
# route.register('ram',ramViewSet)
# route.register('disco', DiscoViewSet)
# route.register('marcaprocesador', MarcaProcesadorViewSet)

# urlpatterns = route.urls

from django.urls import include
from django.conf.urls import url
from .way_two_cbv.views import movies, Practice
from .way_three_fbv.views import movies_list
from .way_one_serializers.routers import router

urlpatterns = [  
    # SERIALIZERS
    url('movies_wone/', include(router.urls)),
    
    # FUNCTION BASED VIEWS
    url('movies_wthree/', movies_list),

    # CLASS BASED VIEWS
    url('movies_wtwo/', movies.as_view()),

    # - - Practice filter methods in ORM Django
    url('practice_filter/', Practice.as_view()),

]
