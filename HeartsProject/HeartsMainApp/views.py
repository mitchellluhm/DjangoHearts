from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from HeartsMainApp.models import Game
from . import forms
from . import card_utility as cu
# from HeartsMainApp.forms import SelectCardForm
# import random



# Create your views here.
def index(request):
    # Create a new Game, assign the hands, set initial values
    # TODO: problem, game refreshes after every submit
    # Two views per one page?
    # can we save and retrieve d?
    # TODO: write d to model, retrieve if not starting a new game, make new if new game

    d = cu.create_context_dict()
    f = forms.SelectCardForm()
    # get or create Game
    try:
        g = Game.objects.get(game_num=779)
        print("got game with specified game_num")
    except ObjectDoesNotExist:
        print("Tried to get Game w/ game_num, but it does not exist")
        print("Now creating game with game_num")
        g = Game.objects.get_or_create(game_num=779,
                                       hand_0_initial=cu.create_initial_hand_str(0, d),
                                       hand_1_initial=cu.create_initial_hand_str(1, d),
                                       hand_2_initial=cu.create_initial_hand_str(2, d),
                                       hand_3_initial=cu.create_initial_hand_str(3, d),
                                       )

    
    d = cu.create_context_dict()
    f = forms.SelectCardForm()


    if request.method == "POST":
        f = forms.SelectCardForm(request.POST)
        if f.is_valid():
            # print(f.cleaned_data['card'])
            f.save(commit=True)
        

    return render(request, 'HeartsMainApp/index.html', context={"all_dict" : d, 'form' : f})
