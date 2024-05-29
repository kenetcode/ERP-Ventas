"""
URL configuration for erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ventas.urls')),
    path('listadoServicio/', include('ventas.urls')),
    path('nuevoServicio/', include('ventas.urls')),
    path('registroVentas/', include('ventas.urls')),
    path('listadoClientes/', include('ventas.urls')),
    path('ingresarCliente/', include('ventas.urls')),
    path('generarInformeVenta/', include('ventas.urls')),
    path('agregarModificarVenta/', include('ventas.urls')),
    path('menuGestor/', include('ventas.urls')),
    path('menuAdministrador/', include('ventas.urls')),
    path('generarFactura/', include('ventas.urls')),
    path('ingresarclienteview/', include('ventas.urls')),
    path('eliminarCliente/<int:id>/', include('ventas.urls')),
    path('consultaClientes/', include('ventas.urls')),
    
    path('editarCliente/', include('ventas.urls')),    
    path('editarClienteView/', include('ventas.urls')),
]   
