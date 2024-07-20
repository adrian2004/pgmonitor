from django.shortcuts import render
from .models import Post
from .utils import get_logged_in_users_count, get_usuarios_total, get_tamanho_base

def home(request):
    logged_in_users = get_logged_in_users_count()
    usuarios_total = get_usuarios_total()
    tamanho_base = get_tamanho_base()
    return render(request, 'monitor/home.html', 
                  {'logged_in_users': logged_in_users, 
                   'usuarios_total': usuarios_total,
                   'tamanho_base': tamanho_base})