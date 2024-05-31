from django.urls import path
from . import views
app_name = 'ventas'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('listadoServicio/', views.listadoServicio_View, name='listadoServicio'),
    path('nuevoServicio/', views.newService_View, name = 'nuevoServicio'),
    path('registroVentas/', views.registroVentas_View, name='registroVentas'),
    path('menuGestor/', views.menuGestor_View, name='menuGestor'),
    path('agregarModificarVenta_View/', views.agregarModificarVenta_View, name='agregarModificarVenta_View'),
    path('listadoClientes/', views.listadoClientes_View, name='listadoClientes'),
    path('consultaClientes/', views.consultarCliente, name='consultaClientes'),
    path('ingresarCliente/', views.ingresarCliente, name='ingresarCliente'),
    path('ingresarclienteview/', views.ingresarCliente_View, name='ingresarclientevista'),
    path('eliminarCliente/<int:id>/', views.eliminarCliente, name='eliminarCliente'),

    path('editarCliente/', views.editarCliente, name='editarCliente'),
    path('editarClienteView/<int:id>/', views.editarCliente_View, name='editarClienteView'),
    path('ingresarServicio/', views.ingresarServicio, name='ingresarServicio'),
    path('eliminarServicio/<int:id>/', views.eliminarServicio, name='eliminarServicio'),
    path('editarServicioView/<int:id>/', views.editarServicio_View, name='editarServicioView'),
    path('editarServicio/', views.editarServicio, name='editarServicio'),
    path('buscarServicio/', views.buscarServicio, name='buscarServicio'),
    path('generarFactura/', views.generarFactura_View, name='generarFactura'),

    path('obtener_servicio/<int:servicio_id>/', views.obtener_servicio, name='obtener_servicio'),
    path('agregarModificarVenta/', views.agregarModificarVenta, name='agregarModificarVenta'), #nueva url
    path('buscarVenta/', views.buscarVenta, name='buscarVenta'),
]   
