from django.shortcuts import render
from .models import Post
from .utils import *
from . import constants

def home(request):
    bases = constants.bases
    dynamic_data = []
    
    for i, base in enumerate(bases):
        dynamic_data.append({
            'base': base,
            'logged_in_users': functions[f'get_usuarios_{i}'](),
            'usuarios_total': functions[f'get_usuarios_total_{i}'](),
            'tamanho_base': functions[f'get_base_tamanho_{i}'](),
            'tamanho_base_tabelas': functions[f'get_base_tamanho_tabelas_{i}']()
        })

    context = {
        'combined_data': zip(bases, dynamic_data)
    }
    return render(request, 'monitor/home.html', context)