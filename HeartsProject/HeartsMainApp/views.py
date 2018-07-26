from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from HeartsMainApp.models import Game
from . import forms
from . import card_utility as CardUtil
# from HeartsMainApp.forms import SelectCardForm
# import random

# Create your views here.
def index(request):

    d = CardUtil.create_context_dict()
    print("card_1 from d" + d['card_1'])
    print("card_50 from d" + d['card_50'])
    f = forms.SelectCardForm()
    CardUtil.dict_from_hand_str(CardUtil.create_initial_hand_str(0, d),
                                CardUtil.create_initial_hand_str(1, d),
                                CardUtil.create_initial_hand_str(2, d),
                                CardUtil.create_initial_hand_str(3, d),
                                )
    # get or create Game
    try:
        # retrieve an already existing game
        g = Game.objects.get(game_num=779)
        print("got game with specified game_num")
    except ObjectDoesNotExist:
        # create the game for first time
        print("Tried to get Game w/ game_num, but it does not exist")
        print("Now creating game with game_num")
        g = Game.objects.get_or_create(game_num=779,
                                       hand_0_initial=CardUtil.create_initial_hand_str(0, d),
                                       hand_1_initial=CardUtil.create_initial_hand_str(1, d),
                                       hand_2_initial=CardUtil.create_initial_hand_str(2, d),
                                       hand_3_initial=CardUtil.create_initial_hand_str(3, d),
                                       )
        # TODO: dynamically load / save context dictionary

    
    d = CardUtil.create_context_dict()
    f = forms.SelectCardForm()


    if request.method == "POST":
        f = forms.SelectCardForm(request.POST)
        if f.is_valid():
            # print(f.cleaned_data['card'])
            f.save(commit=True)
        

    return render(request, 'HeartsMainApp/index.html', context={"all_dict" : d, 'form' : f})
