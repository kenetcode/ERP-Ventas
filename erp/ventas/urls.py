from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('listadoServicio/', views.listadoServicio_View, name='listadoServicio'),
    path('generarInformeVenta/', views.generarInformeVenta_View, name='generarInformeVenta'),
    path('nuevoServicio/', views.newService_View, name = 'nuevoServicio'),
    path('registroVentas/', views.registroVentas_View, name='registroVentas'),
    path('menuGestor/', views.menuGestor_View, name='menuGestor'),
    path('agregarModificarVenta/', views.agregarModificarVenta_View, name='agregarModificarVenta'),
    path('listadoClientes/', views.listadoClientes_View, name='listadoClientes'),
    path('ingresarCliente/', views.ingresarCliente_View, name='ingresarCliente'),
    path('menuAdministrador/', views.menuAdministrador_View, name='menuAdministrador')
]
