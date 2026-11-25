from django import forms
from .models import FarmerProfile


class FarmerProfileForm(forms.ModelForm):

    class Meta:
        model = FarmerProfile

        fields = [
            'phone',
            'location',
            'farm_name'
        ]

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your city or village'
            }),

            'farm_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your farm name'
            }),
        }