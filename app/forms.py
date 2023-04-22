from django import forms

from app.models import PhotoModel


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('photo', 'description')
        labels = {
            'photo': 'Photo',
            'description': 'Description'
        }
