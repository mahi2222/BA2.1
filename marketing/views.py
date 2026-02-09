from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BusinessAssociate

def index(request):
    return render(request, 'marketing/index.html')

def signup(request):
    if request.method == 'POST':
        # Get data from form
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country')
        fee = request.POST.get('fee')
        password = request.POST.get('password')

        # Create Django User for authentication
        if User.objects.filter(username=email).exists():
            return render(request, 'marketing/signup.html', {'error': 'User with this email already exists.'})
        
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)

        # Create and save Business Associate object
        # Note: Ideally we should link this to the User model (e.g., OneToOneField), 
        # but adhering to existing model for now.
        BusinessAssociate.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            pincode=pincode,
            country=country,
            fee_ready_to_pay=fee
            # reference_code removed as it was undefined
        )
        
        # Log the user in
        login(request, user)
        
        return redirect('dashboard')

    return render(request, 'marketing/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'marketing/signin.html', {'error': 'Invalid email or password.'})
            
    return render(request, 'marketing/signin.html')

@login_required(login_url='signin')
def dashboard(request):
    # Retrieve the Business Associate profile based on the logged-in user's email
    try:
        associate = BusinessAssociate.objects.get(email=request.user.email)
    except BusinessAssociate.DoesNotExist:
        associate = None
        
    return render(request, 'marketing/dashboard.html', {'associate': associate})

@login_required(login_url='signin')
def edit_profile(request):
    try:
        associate = BusinessAssociate.objects.get(email=request.user.email)
    except BusinessAssociate.DoesNotExist:
        # Should technically not happen if dashboard works, but handle anyway
        return redirect('dashboard')

    if request.method == 'POST':
        associate.phone = request.POST.get('phone')
        associate.address = request.POST.get('address')
        associate.pincode = request.POST.get('pincode')
        associate.country = request.POST.get('country')
        associate.save()
        return redirect('dashboard')

    return render(request, 'marketing/edit_profile.html', {'associate': associate})

def signout(request):
    logout(request)
    return redirect('index')
