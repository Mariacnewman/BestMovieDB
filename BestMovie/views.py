from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
import requests
import json

# Pagina Login
def index(request):
    return render(request,'BestMovie/Index.html')

# Inicio de sesion
def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user_login = auth.authenticate(username=username, password=password)
    if user_login is not None and user_login.is_active:
        auth.login(request, user_login)
        # Inicio de sesion correcto
        return HttpResponseRedirect("/inicio")
    #else:
        # Inicio de sesion incorrecto
        #return HttpResponseRedirect("/account/invalid/")
    
# Fin de sesion
def logout(request):
    auth.logout(request)
    # Cierre de sesion correcto
    return HttpResponseRedirect("/account/loggedout/")

# Pagina Inicial
def inicio(request):
    if request.user.is_authenticated():
        return render(request,'BestMovie/Inicio.html')

# Vista de Busqueda
def search_movie(request):
    if request.user.is_authenticated():
        query = request.POST.get('query','')
        type_search = request.POST.get('listsel','')
        if query != "":
            if type_search == "Music":
                r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=c9045b016e7d1a992f2af225b251de6e&query='+query)
                movie = r.json()
                return render(request,'BestMovie/search_movie.html',{'movies': [movie]})
            else:
                r = requests.get('https://api.themoviedb.org/3/search/person?api_key=c9045b016e7d1a992f2af225b251de6e&query='+query)
                actor = r.json()
                return render(request,'BestMovie/search_actor.html',{'actors': [actor]})
        else:
            if type_search == "Music":
                r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=c9045b016e7d1a992f2af225b251de6e')
                movie = r.json()
                return render(request,'BestMovie/search_movie.html',{'movies': [movie]})
            else:
                r = requests.get('https://api.themoviedb.org/3/search/person?api_key=c9045b016e7d1a992f2af225b251de6e')
                actor = r.json()
                return render(request,'BestMovie/search_actor.html',{'actors': [actor]})       
        