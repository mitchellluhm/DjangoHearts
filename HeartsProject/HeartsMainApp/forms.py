from django import forms

class SelectCardForm(forms.Form):

    card = forms.CharField()
