from django.shortcuts import render
from .models import Post
from .utils import get_usuarios1, get_usuarios_total1, get_base_tamanho1, get_usuarios2, get_usuarios_total2, get_base_tamanho2

def home(request):
    #BASE 1
    logged_in_users1 = get_usuarios1()
    usuarios_total1 = get_usuarios_total1()
    tamanho_base1 = get_base_tamanho1()
    #BASE 2
    logged_in_users2 = get_usuarios2()
    usuarios_total2 = get_usuarios_total2()
    tamanho_base2 = get_base_tamanho2()
    #RENDER
    return render(request, 'monitor/home.html', 
                  {'logged_in_users1': logged_in_users1, 
                   'usuarios_total1': usuarios_total1,
                   'tamanho_base1': tamanho_base1,
                   'logged_in_users2': logged_in_users2,
                   'usuarios_total2': usuarios_total2,
                   'tamanho_base2': tamanho_base2})