from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
