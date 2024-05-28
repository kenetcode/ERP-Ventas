from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('listadoServicio/', views.listadoServicio_View, name='listadoServicio'),
    path('nuevoServicio/', views.newService_View, name = 'nuevoServicio'),
    path('registroVentas/', views.registroVentas_View, name='registroVentas'),
    path('agregarModificarVenta/', views.agregarModificarVenta_View, name='agregarModificarVenta')
]
