from webbrowser import get
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movies, Types

class movies(APIView):

    def get(self, request):
        data = Movies.objects.all()

        return Response({'data': data.values()})
    
    def post(self, request):

        name, type = request.data['name'], request.data['type']
        
        if not name:
            return Response('name param was not sent')

        if not type:
            return Response('type param was not sent')

        the_type = Types.objects.filter(description = type)
        

        if len(the_type) <= 0 or not the_type:
            return Response('type param was not found, please verify if this exist')

        data = Movies(name = name, type =  the_type[0])
        data.save()

        # imprime: type description
        # return Response({'data': {'name': data.name, 'type': data.type.description} })
        
        # imprime: type id
        return Response({'data': {'name': data.name, 'type': data.type_id} })

class types(APIView):

    def get(self, request):
        data = Types.objects.all()

        return Response({'data': data.values()})
    
    def post(self, request):

        description = request.data['description']
        
        if not description:
            return Response('name param was not sent')
        
        data = Types(description = description)
        data.save()

        # imprime: type description
        # return Response({'data': {'name': data.name, 'type': data.type.description} })
        
        # imprime: type id
        return Response({'description': data.description })