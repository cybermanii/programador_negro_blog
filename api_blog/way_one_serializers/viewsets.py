# # PASO 5

# # despues de haber creado el codigo del archivo serializers.py
# # se importa serializers y viewsets
# from django.db.models import query
# from rest_framework import serializers, viewsets

# # PASO 6
# # se importan las clases creadas en el archivo serializers
# from api_blog.serializers import ComputadoraSerializers, MarcaSerializers, ProcesadorSerializers, ramSerializers, DiscoSerializers, MarcaProcesadorSerializers

# # PASO 7
# # se importan las clases del modelo
# #from tienda.models import Computadora, Marca, Procesador, Ram, Disco, MarcaProcesador

# # Imporataciones para metodos personalizados
# from rest_framework.decorators import action
# from rest_framework.response import Response

# # PASO 8
# # se crea la clase ViewSet para la clase del modelo y la clase correspondiente en serializers
# class ComputadoraViewSet(viewsets.ModelViewSet): # se hereda la clase viewsets
#     queryset = Computadora.objects.all() # se indica la consulta a ejecutar, en este caso SELECT * FROM Computadora usando el ORM de Django
#     serializer_class = ComputadoraSerializers # se indica la clase Serializadora

#     # METODO PERSONALIZADO
#     @action(detail=True, methods=['GET'])
#     def computadorasLenovo(self, request, pk=None):
#         queryset = Computadora.objects.filter(marca_id=pk)
#         serializer = ComputadoraSerializers(queryset, many=True)
#         return Response(serializer.data )

# # PASO 9
# # se crea el archivo urls.py a continuacion

# # se crean las demas clases ViewSets si es necesario
# class MarcaViewSet(viewsets.ModelViewSet):
#     queryset = Marca.objects.all()
#     serializer_class = MarcaSerializers

# class ProcesadorViewSet(viewsets.ModelViewSet):
#     queryset = Procesador.objects.all()
#     serializer_class = ProcesadorSerializers

#     # METODO PERSONALIZADO
#     # ejecutar: http://127.0.0.1:8000/api/procesador/1/marcaprocesador/
#     #                                                ↑              ↑
#     #                                               pk              nombre de la funcion
#     #                                                ↑ 
#     #                                               parametro por el cual realizara la busqueda, no es el ID del elemento
#     @action(detail=True, methods=['GET'])
#     def marcaprocesador(self, request, pk=None):
#         queryset = Procesador.objects.filter(marcaProcesador_id=pk)
#         serializer = ProcesadorSerializers(queryset, many=True)
#         return Response(serializer.data )

# class ramViewSet(viewsets.ModelViewSet):
#     queryset = Ram.objects.all()
#     serializer_class = ramSerializers

# class DiscoViewSet(viewsets.ModelViewSet):
#     queryset = Disco.objects.all()
#     serializer_class = DiscoSerializers

# class MarcaProcesadorViewSet(viewsets.ModelViewSet):
#     queryset = MarcaProcesador.objects.all()
#     serializer_class = MarcaProcesadorSerializers

# ------------------------------------

from rest_framework import viewsets
from ..models import Movies, Types
from .serializers import MoviesSerializer, TypesSerializer

# ViewSets define the view behavior / view set define la conducta de vista
class MoviesViewSet(viewsets.ModelViewSet):
    
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer