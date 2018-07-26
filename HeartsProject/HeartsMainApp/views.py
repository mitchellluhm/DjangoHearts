from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from HeartsMainApp.models import Game
from . import forms
# from HeartsMainApp.forms import SelectCardForm
import random

def make_card_html_tags():
    pre_str = '<img src="/static/images/'
    post_str = '.png" alt="Uh Oh, didnt show!">'
    card_suits = ["clubs", "spades", "hearts", "diamonds"]
    card_vals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    card_htmls = []

    # construct the full string
    for suit in card_suits:
        for val in card_vals:
            temp = pre_str
            temp += val
            temp += "_of_"
            temp += suit
            temp += post_str
            card_htmls.append(temp)

    return card_htmls

def create_context_dict():
    pre_str_key = "card_"
    key_names = []

    for n in range(1,53):
        temp = pre_str_key
        temp += str(n)
        key_names.append(temp)

    cont_dict = dict()
    keys = random.sample(key_names, len(key_names))
    html_tags = make_card_html_tags()
    values = random.sample(html_tags, len(html_tags))

    for n in range(0,52):
        cont_dict.__setitem__(keys[n], values[n])

    return cont_dict

def card_from_html(c_html):
    start = c_html.index("/images/")
    end = c_html.index(".png")
    return c_html[start+8:end]

def card_code_from_card(c):
    code = ""
    of = c.index("_of_")
    c_val = c[0:of]
    c_suit = c[of+4:]

    # assign value part of code
    if c_val == "2":
        code += "2"
    elif c_val == "3":
        code += "3"
    elif c_val == "4":
        code += "4"
    elif c_val == "5":
        code += "5"
    elif c_val == "6":
        code += "6"
    elif c_val == "7":
        code += "7"
    elif c_val == "8":
        code += "8"
    elif c_val == "9":
        code += "9"
    elif c_val == "10":
        code += "X"
    elif c_val == "jack":
        code += "J"
    elif c_val == "queen":
        code += "Q"
    elif c_val == "king":
        code += "K"
    elif c_val == "ace":
        code += "A"
    else:
        print("Error: card_code_from_card()")

    # assign suit part of code
    if c_suit == "spades":
        code += "S"
    elif c_suit == "clubs":
        code += "C"
    elif c_suit == "hearts":
        code += "H"
    elif c_suit == "diamonds":
        code += "D"
    else:
        print("Error: card_code_from_card()")

    return code

def create_initial_hand_str(hand, d):
    hand_str = ""
    cards = []

    if hand == 0:
        cards = ['card_1', 'card_2', 'card_3', 'card_4', 'card_5',
                 'card_6', 'card_7', 'card_8', 'card_9', 'card_10',
                 'card_11', 'card_12',  'card_13',]
    elif hand == 1:
        cards = ['card_14', 'card_15', 'card_16', 'card_17', 'card_18',
                 'card_19', 'card_20', 'card_21', 'card_22', 'card_23',
                 'card_24', 'card_25',  'card_26',]
    elif hand == 2:
        cards = ['card_27', 'card_28', 'card_29', 'card_30', 'card_31',
                 'card_32', 'card_33', 'card_34', 'card_35', 'card_36',
                 'card_37', 'card_38',  'card_39',]
    elif hand == 3:
        cards = ['card_40', 'card_41', 'card_42', 'card_43', 'card_44',
                 'card_45', 'card_46', 'card_47', 'card_48', 'card_49',
                 'card_50', 'card_51',  'card_52',]

    for c in cards:
        hand_str += card_code_from_card(card_from_html(d[c]))

    return hand_str


# Create your views here.
def index(request):
    # Create a new Game, assign the hands, set initial values
    # TODO: problem, game refreshes after every submit
    # Two views per one page?
    # can we save and retrieve d?
    # TODO: write d to model, retrieve if not starting a new game, make new if new game

    # get or create Game
    try:
        g = Game.objects.get(game_num=779)
        print("got game with specified game_num")
    except ObjectDoesNotExist:
        print("Tried to get Game w/ game_num, but it does not exist")
        print("Now creating game with game_num")
        d = create_context_dict()
        f = forms.SelectCardForm()
        h = create_initial_hand_str(0, d)
        g = Game.objects.get_or_create(game_num=779,
                                       hand_0_initial=create_initial_hand_str(0, d),
                                       hand_1_initial=create_initial_hand_str(1, d),
                                       hand_2_initial=create_initial_hand_str(2, d),
                                       hand_3_initial=create_initial_hand_str(3, d),
                                       )

    
    d = create_context_dict()
    f = forms.SelectCardForm()
    create_initial_hand_str(0, d)


    if request.method == "POST":
        f = forms.SelectCardForm(request.POST)
        if f.is_valid():
            # print(f.cleaned_data['card'])
            f.save(commit=True)
        

    return render(request, 'HeartsMainApp/index.html', context={"all_dict" : d, 'form' : f})
