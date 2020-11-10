from django import forms

class InputDataForm(forms.Form):
    teachers = forms.FileField(required=False)

    pictures = forms.FileField(required=False)
