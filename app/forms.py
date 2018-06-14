from django import forms

class ColoriForm(forms.Form):
    codice = forms.CharField(widget = forms.TextInput(attrs={'pattern':'^#(?:[0-9a-fA-F]{3}){1,2}$','title':'Il codice deve iniziare con # e finire con altre 6 lettere'}))
    colore = forms.CharField(label='Nome del colore', max_length="30")