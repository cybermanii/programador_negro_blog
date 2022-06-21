# # PASOS PARA CREAR LA API REST

# # PASO 1
# # importar serializers
# from rest_framework import serializers

# # PASO 2
# # importar las clases del modelo
# from tienda.models import Computadora, Marca, Procesador, Ram, Disco, MarcaProcesador

# # PASO 3
# # crear la clase Serializers para la clase del modelo
# class ComputadoraSerializers(serializers.ModelSerializer ): # heredar la clase serializers
#     class Meta: # crear la clase Meta
#         model = Computadora # indicar el clase del modelo
#         fields = '__all__' # indicar los campos a mostrar en la respuesta de la API, en este caso son todos

# # PASO 4
# # se crea el archivo viewsets.py a continuacion.

# # se crean las demas clases serializers si es necesario
# class MarcaSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Marca
#         fields = '__all__'
# class ProcesadorSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Procesador
#         fields = '__all__'
# class ramSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Ram 
#         fields = '__all__'
# class DiscoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Disco
#         fields = '__all__'

# class MarcaProcesadorSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = MarcaProcesador
        
#         # trae todos los campos de la tabla
#         fields = '__all__'

#         #trae solo los campos indicados en la lista
#         # fields = ['descripcion', 'fechaActualizacion', 'actualizadoPor']

# '''
# NOTA:
# la clase serializer permite convertir 
# los tipos diccionarios, listas, tuplas, etc 
# al formato JSON, XML y otros tipos
# '''

# --------------------------------

from ..models import Movies, Types
from rest_framework import serializers

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        # fields = ['name', 'type']
        fields = '__all__'

class TypesSerializer(serializers.ModelSerializer):
    
    movies = serializers.StringRelatedField(many = True) # serializer relationships

    class Meta:
        model = Types
        # fields = '__all__'
        fields = ['description', 'update_at', 'movies']

    