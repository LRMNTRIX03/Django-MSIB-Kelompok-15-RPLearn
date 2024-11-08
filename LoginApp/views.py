from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        password = request.POST.get('password')
        confirm_password = request.POST.get('conForm')
        flag_bener = True
        if(User.objects.filter(email=request.POST['email']).exists()):
            messages.error(request, "Email sudah terdaftar.")
            flag_bener = False
        if(password != confirm_password):
            messages.error(request, "Password tidak sesuai.")
            flag_bener = False
        if(flag_bener):
            User.objects.create_user(username=request.POST['email'], email=request.POST['email'], password=request.POST['password'])
            messages.success(request, "Akun berhasil dibuat! Silakan login.")
            return redirect('register')  
        else:
            messages.error(request, "Registrasi gagal. Pastikan data diisi dengan benar.")
    else:
        form = RegisterForm()
    
    context = {
        'judul': 'Daftar',
        'LokStyle': 'LoginApp/css/register.css',
        'Scripts': 'LoginApp/js/register.js',
        'forms': form,
    }
    return render(request, 'LoginApp/Register/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('UserWeb:user.dashboard')  
            else:
                messages.error(request, "Email atau password salah.")
    else:
        form = LoginForm()
    
    context = {
        'judul': 'Login',
        'LokStyle': 'LoginApp/css/login.css',
        'Scripts': 'LoginApp/js/login.js',
        'forms': form,
    }
    return render(request, 'LoginApp/Login/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('auth:login')