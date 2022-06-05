from django import forms

class SectorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)  
    profesion=forms.CharField(max_length=40)