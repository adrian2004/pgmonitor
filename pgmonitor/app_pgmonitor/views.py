from django.shortcuts import render
from .models import Post
from .utils import *
from . import constants

def home(request):
    #GET
    logged_in_users = get_usuarios()
    usuarios_total = get_usuarios_total()
    tamanho_base = get_base_tamanho()
    #RENDER
    return render(request, 'monitor/home.html', 
                  {'logged_in_users': logged_in_users, 
                   'usuarios_total': usuarios_total,
                   'tamanho_base': tamanho_base,
                   'base_1': constants.BASE_1})