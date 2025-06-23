from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password

# Create your views here.
def loginView(request):
    storage = get_messages(request)
    list(storage)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):  # Comparación segura
                auth_login(request, user)
                return redirect('crud:invoice_list')
            else:
                messages.error(request, 'Credenciales incorrectas!')
        except User.DoesNotExist:
            messages.error(request, 'Usuario no existe!')
    return render(request, 'login.html', {'messages': messages.get_messages(request)})

def registerView(request):
    name = ""
    lastname = ""
    username = ""
    password = ""
    email = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not User.objects.filter(username=username).exists():
            newUser = User(name=name, lastname=lastname, username=username, password=password, email=email)
            newUser.save()
            return redirect('login:login_join')
        else:
            messages.error(request, 'Usuario ya existe!')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html', {'message': 'Credenciales incorrectas!'})