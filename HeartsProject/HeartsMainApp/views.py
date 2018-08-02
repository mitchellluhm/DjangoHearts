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
    # called on page refresh and submit button pressed
    print("index() function called from views.py")

    form = forms.SelectCardForm()
    # get or create Game
    try:
        # retrieve an already existing game
        g = Game.objects.get(game_num=780)
        print("got game with specified game_num")
        print("g.h0 is " + g.hand_0_initial)

        # create all_dict to use as context dictionary from hands in model
        all_dict = CardUtil.dict_from_hand_str(g.hand_0_initial,
                                               g.hand_1_initial,
                                               g.hand_2_initial,
                                               g.hand_3_initial)

        l = len(g.trick_history)
        if l == 0:
            # find 2C
            current_hand = CardUtil.find_hand_with("2C", g)
            '''
        elif (l % 8) != 0:
            # increment hand
            current_hand = CardUtil.get_next_hand(current_hand, g)
            '''
        elif (l % 8) == 2:
            current_hand = 1
        elif (l % 8) == 4:
            current_hand = 2
        elif (l % 8) == 6:
            current_hand = 3
        else:
            # find trick winner, set hand
            # flush screen
            current_hand = CardUtil.get_next_hand(-2, g)

        print("current_hand: " + str(current_hand))


        # have preceding players play and display cards until it is user's turn
        if current_hand == 0:
            # user's turn
            print("Waiting for user to select a card")
        elif current_hand == 1:
            # left hand's turn
            g.trick_history += g.hand_1_initial[0:2]
        elif current_hand == 2:
            # top hand's turn
            g.trick_history += g.hand_2_initial[0:2]
        elif current_hand == 3:
            # right hand's turn
            g.trick_history += g.hand_3_initial[0:2]

        g.trick_winner = CardUtil.next_hand_from(current_hand)
        g.trick_number += 1
        g.save()

    except ObjectDoesNotExist:
        # create the game for first time
        print("Tried to get Game w/ game_num, but it does not exist")
        print("Now creating game with game_num")
        all_dict = CardUtil.create_context_dict()
        g = Game.objects.get_or_create(game_num=780,
                   hand_0_initial=CardUtil.create_initial_hand_str(0, all_dict),
                   hand_1_initial=CardUtil.create_initial_hand_str(1, all_dict),
                   hand_2_initial=CardUtil.create_initial_hand_str(2, all_dict),
                   hand_3_initial=CardUtil.create_initial_hand_str(3, all_dict))

        # set "trick_winner" to who has 2 of clubs
        # this will the first player to place a card on the first trick
        g.trick_winner = find_hand_with("2C", g)
        # TODO : check this : update model with trick_winner
        g.save()

    if request.method == "POST":
        # select data from trick_history box, and save it to specific instance of g
        form = forms.SelectCardForm(request.POST, instance=g)
        if form.is_valid():
            # print(f.cleaned_data['card'])
            print("Form is valid: " + form.cleaned_data['trick_history'])
            # g.trick_history += form.cleaned_data['trick_history']
            form.save(commit=True)
        

    return render(request, 'HeartsMainApp/index.html',
                  context={"all_dict" : all_dict, 'form' : form})
