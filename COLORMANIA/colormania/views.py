from django.shortcuts import render, redirect
from .models import Color, Pedido, Usuario, Personalizado, Pintura, Producto, Sellador
from django.http import HttpResponse # Importa HttpResponse para casos de depuración o confirmación simple
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
# Create your views here.
def index_colormania(request):
    """
    Vista para la página de inicio del sistema.
    """
    return render(request, 'colormania/index.html')

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.contraseña == password:  # (sé que no está hasheada, pero funciona)
                
                # AQUÍ ESTÁ LA MAGIA: creamos la sesión manualmente
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                request.session['usuario_email'] = usuario.email
                request.session['esta_logueado'] = True  # ← bandera infalible

                messages.success(request, f'¡Bienvenido, {usuario.nombre}!')
                return redirect('index_colormania')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Este email no está registrado.')

    return render(request, 'colormania/login_usuario.html')

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff: 
            auth_login(request, user)
            messages.success(request, f'¡Bienvenido, administrador {user.username}!')
            return redirect('index_admin')  # ¡AQUÍ ESTÁ LA CORRECCIÓN!
            # o 'index_admin' si prefieres ese nombre
        else:
            messages.error(request, 'Usuario o contraseña de administrador incorrectos.')

    return render(request, 'colormania/login_admin.html')




def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        contraseña = request.POST.get('contraseña')
        confirmar_contraseña = request.POST.get('confirmar_contraseña')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('codigo_postal')
        calle = request.POST.get('calle')
        num_domicilio = request.POST.get('num_domicilio')
        detalles = request.POST.get('detalles', 'INFORMACION DEL DOMICILIO') # Usa el default si no se envía

        # Validaciones
        if contraseña != confirmar_contraseña:
            messages.error(request, 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')
            return render(request, 'colormania/registro.html') # Vuelve a renderizar con el mensaje

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este email ya está registrado. ¿Ya tienes una cuenta?')
            return render(request, 'colormania/registro.html')

        try:
            nuevo_usuario = Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                contraseña=contraseña, # RECUERDA: EN PRODUCCIÓN, DEBES HASHEAR LAS CONTRASEÑAS
                pais=pais,
                estado=estado,
                ciudad=ciudad,
                codigo_postal=codigo_postal,
                calle=calle,
                num_domicilio=num_domicilio,
                detalles=detalles
            )
            messages.success(request, f'¡Bienvenido/a {nombre}! Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login_usuario') # Redirige al login después de un registro exitoso
        except Exception as e:
            messages.error(request, f'Ocurrió un error al intentar registrarte: {e}')

    return render(request, 'colormania/registro.html')

def index(request):
    return render(request, 'colormania/index.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all().order_by('nombre')
    context = {
        'usuarios': usuarios
    }

    return render(request, 'colormania/admin/usuarios.html', context)


def index_admin(request):
    return render(request, 'colormania/admin/index_admin.html')  # página principal del admin

def admin_pinturas(request):
    return render(request, 'colormania/admin/pinturas.html')

def admin_productos(request):
    return render(request, 'colormania/admin/productos.html')

def admin_selladores(request):
    return render(request, 'colormania/admin/selladores.html')

def admin_colores(request):
    return render(request, 'colormania/admin/colores.html')

# Cerrar sesión del admin
def logout_admin(request):
    logout(request)
    messages.success(request, "¡Sesión de administrador cerrada!")
    return redirect('index_colormania')

def logout_usuario(request):
    try:
        del request.session['usuario_id']
        del request.session['usuario_nombre']
        del request.session['esta_logueado']
    except:
        pass
    messages.success(request, "¡Sesión cerrada correctamente!")
    return redirect('index_colormania')

def ver_pinturas(request):
    pinturas = Pintura.objects.all().order_by('nombre')
    
    return render(request, 'colormania/user/ver_pinturas.html', {
        'productos': pinturas  # el template usa 'productos', así que le pasamos eso
    })
    
def ver_selladores(request):
    selladores = Pintura.objects.all()  # Cambia por tu modelo de selladores cuando lo tengas
    return render(request, 'colormania/user/ver_selladores.html', {'productos': selladores})

def ver_productos(request):
    productos = Pintura.objects.all()  # Cambia por tu modelo real cuando lo tengas
    return render(request, 'colormania/user/ver_productos.html', {'productos': productos})