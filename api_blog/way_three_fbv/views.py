from django import views


# FUNCTION BASED VIEWS / vistas basadas en funciones

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Movies

from ..way_one_serializers.serializers import MoviesSerializer

@api_view(['GET', 'POST'])
def movies_list(request):
    try:

        movies =  Movies.objects.all()

        if request.method == 'GET':
            serializer = MoviesSerializer(movies, many = True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = MoviesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    except Exception as ex:
        return Response({ 'error': ex })

@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, pk):
    '''
    retrieve, update or delete a movie
    '''
    
    try:
        movie = Movies.objects.get(pk = pk)

    except movie.DoesNotExist:
        return Response({ 'error': f'the object with id {pk} does not exist'}, status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MoviesSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)