from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Crop, Disease, Prediction, UploadedLeafImage


def home(request):
    return render(request, 'core/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'core/register_success.html')

    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {
        'form': form
    })
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
           login(request, user)
           return redirect('dashboard')

        return render(request, 'core/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'core/login.html')  


@login_required
def farmer_dashboard(request):
    return render(request, 'core/dashboard.html')  

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('leaf_image')

        if image:
            UploadedLeafImage.objects.create(
                user=request.user,
                image=image
            )

            return render(
                request,
                'core/upload_image.html',
                {'success': 'Leaf image uploaded successfully!'}
            )

        return render(
            request,
            'core/upload_image.html',
            {'error': 'Please select an image.'}
        )

    return render(request, 'core/upload_image.html')