from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User

# Create your views here.
def loginView(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if users.filter(username=username, password=password).exists():
            return redirect('crud:crud_list')
    else:
        messages.error(request, 'Usuario ya existe!')
    
    return render(request, 'login.html')

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