from django.shortcuts import render
from .models import Post
from .utils import get_logged_in_users_count
from .utils import get_usuarios_total

def home(request):
    logged_in_users = get_logged_in_users_count()
    usuarios_total = get_usuarios_total()
    return render(request, 'monitor/home.html', {'logged_in_users': logged_in_users, 'usuarios_total': usuarios_total})