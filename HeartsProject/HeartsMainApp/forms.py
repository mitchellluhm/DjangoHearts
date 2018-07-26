from django import forms
from HeartsMainApp.models import Game

class SelectCardForm(forms.ModelForm):

    # validators go here

    class Meta():
        # just one model for now
        model = Game
        # TODO : dynamically decide which field we need to include
        # this will be based off values of previously filled in fields
        fields = ('trick_history',)

    #card = forms.CharField()
