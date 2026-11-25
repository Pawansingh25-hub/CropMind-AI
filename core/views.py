from .weather_service import get_weather, get_farming_advice
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Crop, Disease, Prediction, UploadedLeafImage, FarmerProfile
from .ai_predictor import predict_leaf_disease
from .forms import FarmerProfileForm
from pathlib import Path
from PIL import Image, UnidentifiedImageError


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
        
        
# Validate image file size (maximum 5 MB)
        if image.size > 5 * 1024 * 1024:
           return render(
              request,
              'core/upload_image.html',
              {'error': 'Image size must be less than 5 MB.'}
            )

        # Validate file extension
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.webp']
        file_extension = Path(image.name).suffix.lower()

        if file_extension not in allowed_extensions:
          return render(
            request,
            'core/upload_image.html',
            {'error': 'Only JPG, JPEG, PNG and WEBP images are allowed.'}
          )

# Verify actual image content
        try:
          image.seek(0)

          with Image.open(image) as img:
           img.verify()

          image.seek(0)

        except (UnidentifiedImageError, OSError, ValueError):
          return render(
          request,
          'core/upload_image.html',
          {'error': 'Invalid or corrupted image. Please upload a valid image.'}
          )


        if image:
            uploaded_image = UploadedLeafImage.objects.create(
                user=request.user,
                image=image
            )

            try:
                result = predict_leaf_disease(uploaded_image.image.path)
                display_name = result['class_name'].replace('Tomato___', '').replace('_', ' ')
                disease = Disease.objects.filter(
                name__iexact=f"Tomato {display_name}"
                ).first()
                uploaded_image.predicted_disease = display_name
                uploaded_image.confidence = result['confidence']
                uploaded_image.save(update_fields=['predicted_disease', 'confidence'])

                return render(
                    request,
                    'core/upload_image.html',
                    {
                        'success': 'Leaf image uploaded successfully!',
                        'uploaded_image': uploaded_image,
                        'prediction': display_name,
                        'confidence': result['confidence'],
                        'symptoms': disease.symptoms if disease else '',
                        'causes': disease.causes if disease else '',
                        'prevention': disease.prevention if disease else '',
                        'management': disease.management if disease else '',
                    }
                )

            except Exception as e:
                print(f'AI prediction error: {e}')
                return render(
                    request,
                    'core/upload_image.html',
                    {
                        'uploaded_image': uploaded_image,
                        'error': 'Image uploaded, but AI prediction failed. Please try again.'
                    }
                )

        return render(
            request,
            'core/upload_image.html',
            {'error': 'Please select an image.'}
        )

    return render(request, 'core/upload_image.html')

@login_required
def prediction_history(request):
    predictions = UploadedLeafImage.objects.filter(
        user=request.user
    ).exclude(
        predicted_disease__isnull=True
    ).order_by('-uploaded_at')

    return render(
        request,
        'core/prediction_history.html',
        {'predictions': predictions}
    )

@login_required
def delete_prediction(request, prediction_id):

    if request.method == 'POST':
        prediction = get_object_or_404(
            UploadedLeafImage,
            id=prediction_id,
            user=request.user
        )

        # Delete uploaded image from media storage
        if prediction.image:
            prediction.image.delete(save=False)

        # Delete prediction record from database
        prediction.delete()

    return redirect('prediction_history')

@login_required
def weather_dashboard(request):

    weather = None
    error = None

    if request.method == 'POST':

        city = request.POST.get('city', '').strip()

        if city:

            result = get_weather(city)

            if 'error' in result:
                error = result['error']

            else:
                weather = result

                extra_info = get_farming_advice(weather)

                weather['condition'] = extra_info['condition']
                weather['advice'] = extra_info['advice']

        else:
            error = 'Please enter a city name.'

    return render(
        request,
        'core/weather.html',
        {
            'weather': weather,
            'error': error
        }
    )
    
@login_required
def farmer_profile(request):

    profile, created = FarmerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = FarmerProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return render(
                request,
                'core/farmer_profile.html',
                {
                    'form': FarmerProfileForm(instance=profile),
                    'profile': profile,
                    'success': 'Profile updated successfully!'
                }
            )

    else:
        form = FarmerProfileForm(instance=profile)

    return render(
        request,
        'core/farmer_profile.html',
        {
            'form': form,
            'profile': profile
        }
    )