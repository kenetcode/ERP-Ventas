from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña inválidos'})
    else:
        return render(request, 'login.html')
    
def listadoServicio_View(request):
    return render(request, 'listadoServicio.html')

def newService_View(request):
    return render(request, 'nuevoServicio.html')

def registroVentas_View(request):
    return render(request, 'registroVentas.html')

def listadoClientes_View(request):
    lista = Cliente.objects.all()
    datos = {'clientes' : lista}
    return render(request, 'listadoClientes.html', datos)

@login_required
def ingresarCliente(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tipocliente = request.POST.get('tipo-cliente')
        nombrecomercial = request.POST.get('nameComercial')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        cliente = Cliente(nombre=name, tipocliente=tipocliente, nombrecomercial=nombrecomercial, telefono=telefono, email=email, direccion=direccion)
        cliente.save()
        return redirect('/ingresarclienteview/')

def ingresarCliente_View(request):
    return render(request, 'ingresarCliente.html')

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/listadoClientes/')

def consultarCliente(request):
    if request.method == 'POST':
        name = request.POST.get('nombre')
        cliente = Cliente.objects.filter(nombre=name)
        return render(request, 'listadoClientes.html', {'clientes': cliente})

def generarInformeVenta_View(request):
    return render(request, 'generarInformeVenta.html')

def agregarModificarVenta_View(request):
    return render(request, 'agregarModificarVenta.html')

def menuGestor_View(request):
    return render(request, 'menuGestor.html')

