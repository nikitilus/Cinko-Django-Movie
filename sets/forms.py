from django import forms
from .models import Set, Film

  
  
class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ["name", "description", "image", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Название категории"}),
            "description": forms.Textarea(attrs={"class": "form-control", 
                                                 "placeholder": "Описание категории"}),
            "image": forms.FileInput(attrs={"class": "form-control-file"}),
            
            "slug": forms.TextInput(attrs={"class": "form-control", 
                                           "placeholder": "ID категории"}),
        }

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["set", "title", "description", "release_date", "image", "slug"]
        widgets = {
            "set": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Название фильма"}),
            "description": forms.Textarea(attrs={"class": "form-control",
                                                 "placeholder": "Описание фильма"}),
            "release_date": forms.DateInput(attrs={"class": "form-control",
                                                   "type": "date"}),
            "image": forms.FileInput(attrs={"class": "form-control-file"}),
            "slug": forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "ID фильма"}),
        }