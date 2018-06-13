from django import forms

class ColoriForm(forms.Form):
    codice = forms.CharField(label='Codice esadecimale', max_length="7")
    colore = forms.CharField(label='Nome del colore', max_length="30")