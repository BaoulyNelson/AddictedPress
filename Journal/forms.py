from django import forms
from .models import Testimonial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Champ email obligatoire
    first_name = forms.CharField(max_length=30, required=True)  # Prénom obligatoire
    last_name = forms.CharField(max_length=30, required=True)  # Nom obligatoire

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
