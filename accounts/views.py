from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()

# Create your views here.
def login_view(request):
    data = None
    if request.method == 'POST':
        username = request.POST.get('Username')
        pawd = request.POST.get('password')
        try:
            data = User.objects.get(username = username )
            print(data)
        except Exception as e:
            messages.error(request, 'Username dosen\'t exists')
        if data:
            user = authenticate(request, username = username,password = pawd)
            if user:
                print('login')
                login(request , user)
                if user.is_staff:
                    return redirect('dash-board')
                else:
                    return redirect('quiz_home') 
            else:
                messages.error(request, 'password is incorrect')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_pass')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone_no = request.POST.get('phone_no')

        if password != confirm_password:
            messages.error(request , 'password didnt matched with confirm password')
            return redirect('signup')
        try:
            validate_password(password)

        except Exception as e:
            for error in e.messages:
                messages.error(request, error)
            return redirect('signup')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_no = phone_no
        )
        user.save()
        return redirect('login')

    return render(request, 'signup.html')
