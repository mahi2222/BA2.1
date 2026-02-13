from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BusinessAssociate


# 1. Home Page (located in Root)
def index(request):
    return render(request, 'index.html')


# 2. Signup Logic
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')

        if User.objects.filter(username=email).exists():
            return render(request, 'marketing/signup.html', {'error': 'User exists'})

        # Create Auth User
        user = User.objects.create_user(username=email, email=email, password=password, first_name=fname,
                                        last_name=lname)

        # Create BA Profile
        BusinessAssociate.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            pincode=request.POST.get('pincode'),
            country=request.POST.get('country'),
            fee_ready_to_pay=request.POST.get('fee')
        )

        login(request, user)
        return redirect('dashboard')  # Redirect to NAME, not path

    return render(request, 'marketing/signup.html')


# 3. Signin Logic
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'marketing/signin.html', {'error': 'Invalid Login'})

    return render(request, 'marketing/signin.html')


# 4. Dashboard (Protected)
@login_required(login_url='signin')
def dashboard(request):
    try:
        associate = BusinessAssociate.objects.get(email=request.user.email)
    except BusinessAssociate.DoesNotExist:
        associate = None
    return render(request, 'marketing/dashboard.html', {'associate': associate})


# 5. Signout
def signout(request):
    logout(request)
    return redirect('index')