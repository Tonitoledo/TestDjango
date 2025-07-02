import logging
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

logger = logging.getLogger(__name__)

# Create your views here.
def loginView(request):
    storage = get_messages(request)
    list(storage)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor ingrese ambos campos')
            logger.warning('Intento de login con campos vacíos')
            return render(request, 'login.html')
        
        User = get_user_model()

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):  # Comparación segura
                auth_login(request, user)
                return redirect('crud:invoice_list')
            else:
                messages.error(request, 'Credenciales incorrectas!')
                logger.warning(f'Contraseña incorrecta para el usuario: {username}')
        except User.DoesNotExist:
            messages.error(request, 'Usuario no existe')
            logger.warning(f'Intento de login con usuario inexistente: {username}')
            
        except Exception as e:
            messages.error(request, 'Error en el sistema')
            logger.error(f'Error durante el login: {str(e)}', exc_info=True)

    return render(request, 'login.html', {'messages': messages.get_messages(request)})

def registerView(request):
    first_name = ""
    last_name = ""
    username = ""
    password = ""
    email = ""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not User.objects.filter(username=username).exists():
            newUser = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
            newUser.save()
            return redirect('login:login_join')
        else:
            messages.error(request, 'Usuario ya existe!')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html', {'message': 'Credenciales incorrectas!'})