from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('listadoServicio/', views.listadoServicio_View, name='listadoServicio'),
    path('generarInformeVenta/', views.generarInformeVenta_View, name='generarInformeVenta')
]
