from django.urls import path
from app_pgmonitor import views
from django.contrib import admin

urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
