from django import forms
from .models import Genre, Track

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru' , 'name_en' , 'discription']
