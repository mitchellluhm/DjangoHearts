from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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

def send_json(d):
    return JsonResponse(d)

# Create your views here.
def index(request):
    context_dict = {
        #                     V this syntax is different when sending it thru cont
        "ins_me" : '<img src="/static/images/5_of_clubs.png" alt="Uh Oh, didnt show!">',
        "ins_me2" : "<em> HEY </em>",
    } 
    d = create_context_dict()
    # d.__setitem__('all', d)
    # print(d['all'])
    # send_json(d)
    return render(request, 'HeartsMainApp/index.html', context={"all_dict" : d})
