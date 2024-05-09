from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, VerificationCode
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
from .decorators import authenticated
from socket import gaierror


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email=email).first()
        if password1 != password2 or not email.strip():
            return redirect('register')
        elif ex_user:
            return HttpResponse('<h1>This email was previously registered</h1>')
        else:
            user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name,
                                                  password=password1, is_active=False)
            random_verify_code = random.randint(100000, 999999)
            VerificationCode.objects.create(user=user, verification_code=random_verify_code)
            try:
                send_mail('VerificationCode', f'Your verification code is {random_verify_code}', settings.EMAIL_HOST_USER,
                          [email], fail_silently=False)
            except gaierror as e:
                user = CustomUser.objects.get(email=email)
                user.delete()
                return HttpResponse('<h1>Not internet connection or error code</h1>')
            return redirect('verify', id=user.id)
    return render(request, 'auth/register.html')


def verification(request, id):
    if request.method == 'POST':
        user_verification_code = request.POST.get('verification_code')
        user = CustomUser.objects.filter(id=id).first()
        verify_code = VerificationCode.objects.filter(user=user).first()
        if user.is_active and int(user_verification_code) == verify_code.verification_code:
            return redirect('new_password', id=user.id)
        elif int(user_verification_code) == verify_code.verification_code:
            user.is_active = True
            user.save()
            login(request=request, user=user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Verification code is incorrect </h1>')
    else:
        return render(request, 'auth/verification.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            random_code = random.randint(100000, 999999)
            VerificationCode.objects.create(user=user, verification_code=random_code)
            send_mail('VerificationCode', f'Your verification code is {random_code}', settings.EMAIL_HOST_USER,
                      [email], fail_silently=False)
            return redirect('verify', id=user.id)
        else:
            return HttpResponse("<h1>User not found</h1>")
    else:
        return render(request, 'auth/forgot_password.html')


def new_password(request, id):
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = CustomUser.objects.filter(id=id).first()
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'auth/new_password.html')


@authenticated
def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_authenticate = authenticate(request, email=email, password=password)
        user = CustomUser.objects.filter(email=email).first()
        print(user.password)
        if user.password == password:
            login(request, user)
            return redirect('home')
        elif user_authenticate:
            login(request, user_authenticate)
            return redirect('home')
        else:
            return HttpResponse('<h1>You entered an email or password incorrectly </h1>')
    return render(request=request, template_name='auth/login.html')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
