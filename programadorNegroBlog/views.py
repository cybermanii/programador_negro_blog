from django.core.files.storage import FileSystemStorage
from datetime import datetime
import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, request, response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .settings import USER_SESSIONS


@csrf_exempt
def index(request):

    # este script cuenta el numero de veces que
    # un usuario entra o visita una vista en especifico.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # recibe el nombre de usuario logueado en la aplicacion
    userSession = request.session['user']

    return render(request, "ProgNegroBlog/indexView.html", {'userSession': userSession, 'numVisits': num_visits, 'numVisitsApp': len(USER_SESSIONS), 'usersLogged': USER_SESSIONS})
    #                |              |
    #           peticion      		vista

    # pagina de tutoriales python


def tecnologias(request):

    userSession = request.session['user']
    if userSession == None:
        return render(request, 'ProgNegroBlog/login/loginView.html')
    return render(request, 'ProgNegroBlog/tecnologiasView.html', {'userSession': userSession})


def pythonPagina(request):
    userSession = request.session['user']
    return render(request, "ProgNegroBlog/pythonView.html", {'userSession': userSession})

    # pagina de tutoriales javascript


def javascriptPagina(request):
    userSession = request.session['user']
    return render(request, "ProgNegroBlog/javascriptView.html", {'userSession': userSession})

    # pagina de tutoriales generales


def tutorialesPagina(request):
    userSession = request.session['user']
    return render(request, "ProgNegroBlog/tutorialesView.html", {'userSession': userSession})

    # pagina de capitulos de alguna serie


def capitulosPagina(request):
    userSession = request.session['user']
    return render(request, "ProgNegroBlog/capitulosView.html", {'userSession': userSession})

# --- creacion de FORMULARIOS -------------


def contacto(request):
    userSession = request.session['user']
    if request.method == 'POST':
        return render(request, "ProgNegroBlog/graciasContactoView.html")

    return render(request, "ProgNegroBlog/contactoView.html", {'userSession': userSession})


# Paso de argumentos por URL


def argumentos(request):
    # http://127.0.0.1:8000/argumentos/?numeros=1,2,3
    numeros = request.GET['numeros']
    ordenados = [int(numero) for numero in numeros.split(',')]
    nordenados = sorted(ordenados)

    data = {
        'status': 'ok',
        'numeros': nordenados,
        'message': '¡ordenados con exito!'
    }
    # return HttpResponse(f'Hola Mundo {numeros}') # response simple
    # return HttpResponse(str(ordenados), content_type='application/json') # imprime los valores en formato JSON
    return HttpResponse(
        json.dumps(data, indent=2),  # convierte el diccionario a formato json
        content_type='application/json'  # indica el formato en que deve imprimirse
    )

# paso de argumoentos con valores predefinidos en url.py


def validacion(request, name, edad):
    mensaje = ''
    if edad < 18:
        mensaje = f'{name}, you are not allowed here'
    else:
        mensaje = f'{name}, you are welcome'

    return HttpResponse(mensaje)


# Envio de contenido

datos = [
    {
        'descripcion': 'IMAGEN UNO',
        'fecha': str(datetime.now()),
        'imagen': 'https://picsum.photos/id/237/200/300'
    },
    {
        'descripcion': 'IMAGEN DOS',
        'fecha': str(datetime.now()),
        'imagen': 'https://picsum.photos/seed/picsum/200/300'
    },
    {
        'descripcion': 'IMAGEN TRES',
        'fecha': str(datetime.now()),
        'imagen': 'https://picsum.photos/200/300?grayscale'
    }
]


def data(request):
    contenido = []
    for dato in datos:
        contenido.append(
                '''
			<p>
			<strong>{descripcion}</strong><br>
			<b>{fecha}</b> <br>
			<img src="{imagen}" /> <br>
			</p>
			'''.format(**dato))
    return HttpResponse('<br>'.join(contenido))


# @csrf_exempt
def loginView(request):

    # if request.POST:
    if request.method == 'POST':

        username = request.POST.get('user')
        password = request.POST.get('pass')

        print("USERNAME:"+str(username))

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = username

            if username not in USER_SESSIONS:  # si el usuario logueado actual no esta en la session
                USER_SESSIONS.append(username)
            return render(request, "ProgNegroBlog/indexView.html", {'userSession': request.session['user'], 'numVisitsApp': len(USER_SESSIONS)})

        else:
            errorMessageLogin = "user or password incorrect"
            return render(request, "ProgNegroBlog/login/loginView.html", {'errorLogin': errorMessageLogin})
    return render(request, "ProgNegroBlog/login/loginView.html")


def loadFile(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        myfile = request.FILES.get('archivo')
        fs = FileSystemStorage()
        print(myfile.name)
        print(myfile)
        filename = fs.save(myfile.name, myfile)
    #uploaded_file_url = fs.url(filename)

    return render(request, 'ProgNegroBlog/archivosModule/loadFileView.html')
