from django.shortcuts import redirect, render
from .models import User

# Create your views here.
def loginView(request):
    users = User.objects.all()
    if request.method == 'POST':
        print("Dentro")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if users.filter(username=username, password=password).exists():
            print("Login correcto")
            return redirect('crud:crud_list')
    else:
        print("OPPS")
        return render(request, 'login.html', {'message': 'Credenciales incorrectas!'})
    
    return render(request, 'login.html')