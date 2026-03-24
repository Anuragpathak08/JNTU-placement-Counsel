from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.GET.get('username')
        pawd = request.GET.get('password')
        user = authenticate(request, username = username,password = pawd)
        if user:
            login(request , user)
            

    return render(request, 'accounts/login.html')
def logout_view(request):
    return render(request, 'accounts/logout.html')

def register_view(request):
    return render(request, 'accounts/register.html')    
