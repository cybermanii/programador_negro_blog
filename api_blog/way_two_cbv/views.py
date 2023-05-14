from ast import Try
from types import TracebackType
from webbrowser import get
from django.shortcuts import render
from ..utilities.utils import json_serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import api_settings

from ..models import Movies, Types

class movies(APIView):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
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

class Practice(APIView):

    def get(self, request):
        try:
            iexact_value = self.request.query_params.get('iexact')
            icontains_value = self.request.query_params.get('icontains')
            startswith_value = self.request.query_params.get('startswith')
            endswith_value = self.request.query_params.get('endswith')
            lt_value = self.request.query_params.get('lt')
            gt_value = self.request.query_params.get('gt')
            gte_value = self.request.query_params.get('gte')
            union_value = self.request.query_params.get('union')
            join_value = self.request.query_params.get('join')

            if iexact_value is not None:
                '''
                Busca valores en su misma longitud de caracteres que coincidan sin tener en cuenta mayusculas o minusculas, es igual a = como en SQL
                '''
                data= Movies.objects.filter(name__iexact = iexact_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': data.values()})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif icontains_value is not None:
                '''
                Busca valores que contengan el valor buscado en alguna de sus partes, es igual a LIKE como en SQL, ejemplo: "%valor%"
                '''
                data= Movies.objects.filter(name__icontains = icontains_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': data.values()})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif startswith_value is not None:
                '''
                Busca registros que empiecen con el valor buscado, como LIKE en SQL, ejemplo: "valor%"
                '''
                data= Movies.objects.filter(name__startswith = startswith_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': json_serializer(data)})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif endswith_value is not None:
                '''
                Busca registros que terminen con el valor buscado, como LIKE en SQL, ejemplo: "%valor"
                '''
                data= Movies.objects.filter(name__endswith = endswith_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': json_serializer(data)})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif lt_value is not None:
                '''
                Busca registros que terminen con el valor buscado, como LIKE en SQL, ejemplo: "%valor"
                '''
                data= Movies.objects.filter(power_level__lt = lt_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': json_serializer(data)})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif gt_value is not None:
                '''
                Busca registros que terminen con el valor buscado, como LIKE en SQL, ejemplo: "%valor"
                '''
                data= Movies.objects.filter(power_level__gt = gt_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': json_serializer(data)})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            elif gte_value is not None:
                '''
                Busca registros que terminen con el valor buscado, como LIKE en SQL, ejemplo: "%valor"
                '''
                data= Movies.objects.filter(power_level__gte = gte_value)

                if data.exists():
                    return Response({'type': 'ok', 'detail': json_serializer(data)})
                else:
                    return Response({'type': 'ok', 'detail': 'does not exist'})
            else:
                data= Movies.objects.all()
                return Response({'type': 'ok', 'detail': json_serializer(data)})

            return Response({'type':'error', 'detail':'there was a error'})

        except Exception as e:
            return Response({'type':'error', 'detail': e})