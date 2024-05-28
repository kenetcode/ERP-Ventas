from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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

def agregarModificarVenta_View(request):
    return render(request, 'agregarModificarVenta.html')