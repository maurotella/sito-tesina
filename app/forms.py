from django import forms

class ColoriForm(forms.Form):
    codice = forms.TextInput(label='Codice esadecimale', max_length="7", attrs={'pattern':'#[0-9a-f]{6}','title':'Il codice deve iniziare con # e finire con altre 6 lettere'})
    colore = forms.TextInput(label='Nome del colore', max_length="30")