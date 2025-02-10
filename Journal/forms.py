from django import forms
from .models import Testimonial
from django.contrib.auth.models import User


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }



# Formulaire pour mettre à jour le profil de l'utilisateur
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

