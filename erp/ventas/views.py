from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Servicio, Venta
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña inválidos'})
    else:
        return render(request, 'login.html')
    
@login_required    
def listadoServicio_View(request):
    servicio = Servicio.objects.all()
    print(Servicio.descripcion)
    return render(request, 'listadoServicio.html', {'servicios': servicio})

@login_required 
def newService_View(request):
    return render(request, 'nuevoServicio.html')

@login_required 
def registroVentas_View(request):
    return render(request, 'registroVentas.html')

@login_required 
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
        return redirect('/listadoClientes/')

@login_required
def ingresarCliente_View(request):
    return render(request, 'ingresarCliente.html')

@login_required 
def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/listadoClientes/')

@login_required 
def consultarCliente(request):
    if request.method == 'POST':
        name = request.POST.get('nombre')
        if(name == ''):
            return redirect('/listadoClientes/')
        cliente = Cliente.objects.filter(nombre=name)
        return render(request, 'listadoClientes.html', {'clientes': cliente})

@login_required 
def agregarModificarVenta_View(request):
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()
    return render(request, 'agregarModificarVenta.html', {'clientes': clientes, 'servicios': servicios})

@login_required
def agregarModificarVenta(request): #Nuevo metodo
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        metodopago = request.POST.get('metodopago')
        cliente = Cliente.objects.get(id=request.POST.get('cliente'))
        total = request.POST.get('total')
        venta = Venta(fecha=fecha, metodopago=metodopago, cliente=cliente, total=total)
        venta.save()      
        request.session['venta_id'] = venta.id
        return redirect('/generarFactura/')

def obtener_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    data = {'nombre': servicio.nombre, 'descripcion': servicio.descripcion, 'precio': servicio.costo}
    return JsonResponse(data)

@login_required 
def menuGestor_View(request):
    return render(request, 'menuGestor.html')

def menuAdministrador_View(request):
    return render(request, 'menuAdministrador.html')

"""def obtenerServicios(request):
    servicios = []
    for key in request.POST.keys():
        if key.startswith('servicios['):
            id_servicio = request.POST.get(key)
            servicios.append(id_servicio)
    print(servicios)
    request.session['servicios_id'] = servicios """

def generarFactura_View(request):
    servicios = []
    for key in request.POST.keys():
        if key.startswith('servicios['):
            id_servicio = request.POST.get(key)
            servicios.append(get_object_or_404(Servicio, id=id_servicio))
    print(servicios)
    print("Hola Mundo")
    venta_id = request.session.get('venta_id')
    venta = get_object_or_404(Venta, id=venta_id)  
    subtotal = round((venta.total/1.13), 2)
    iva = round(subtotal*0.13, 2)
    context = {'venta': venta, 'subtotal': subtotal,'iva':iva, 'servicios': servicios}
    print("AVCC")
    return render(request, 'generarFactura.html', context)

    
@login_required
def editarCliente(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        cliente = Cliente.objects.get(id=id)
        name = request.POST.get('name')
        tipocliente = request.POST.get('tipo-cliente')
        nombrecomercial = request.POST.get('nameComercial')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        cliente.nombre = name
        cliente.tipocliente = tipocliente
        cliente.nombrecomercial = nombrecomercial
        cliente.telefono = telefono
        cliente.email = email
        cliente.direccion = direccion
        cliente.save()
        return redirect('/listadoClientes/')
    return render(request, 'editarCliente.html', {'cliente': cliente})

@login_required
def editarCliente_View(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'editarCliente.html', {'cliente': cliente})

@login_required
def ingresarServicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        Servicio.objects.create(nombre=nombre, descripcion=descripcion, costo=costo)
        return redirect('listadoServicio/')
    else:
        return redirect('listadoServicio/')

@login_required
def eliminarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('/listadoServicio/')

def editarServicio_View(request, id):
    servicio = Servicio.objects.get(id=id)
    return render(request, 'editarServicio.html', {'servicios': servicio})

def editarServicio(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        servicio = Servicio.objects.get(id=id)
        nombre = request.POST.get('name')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        servicio.nombre = nombre
        servicio.descripcion = descripcion
        servicio.costo = costo
        servicio.save()
        return redirect('/listadoServicio/')
    return render(request, 'editarServicio.html', {'servicios': servicio})

def buscarServicio(request):
    if request.method == 'POST':
        buscar = request.POST.get('servicio')
        if(buscar==""):
            return redirect('/listadoServicio/')
        else:
            servicio = Servicio.objects.filter(nombre=buscar)
            return render(request, 'listadoServicio.html', {'servicios': servicio})
    
    

