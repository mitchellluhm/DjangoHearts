import random

def make_card_html_tags(exists=False, cards_order=[]):
    pre_str = '<img src="/static/images/'
    post_str = '.png" alt="Uh Oh, didnt show!">'
    card_suits = ["clubs", "spades", "hearts", "diamonds"]
    card_vals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    card_htmls = []

    # construct the full string
    c = -1 
    for suit in card_suits:
        for val in card_vals:
            c += 1
            temp = pre_str
            if not exists:
                temp += val
                temp += "_of_"
                temp += suit
            else:
                temp += cards_order[c]

            temp += post_str
            card_htmls.append(temp)

    return card_htmls

def create_context_dict(exists=False, card_order=[]):
    pre_str_key = "card_"
    key_names = []

    for n in range(1,53):
        temp = pre_str_key
        temp += str(n)
        key_names.append(temp)

    cont_dict = dict()
    # i don't think shuffling the keys matter for dict
    #keys = random.sample(key_names, len(key_names))
    keys = key_names
    if not exists:
        html_tags = make_card_html_tags()
        values = random.sample(html_tags, len(html_tags))
    else:
        html_tags = make_card_html_tags(True, card_order)
        values = html_tags

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
    else:
        print("Error: create_initial_hand_str(), wrong hand argument specified")

    for c in cards:
        hand_str += card_code_from_card(card_from_html(d[c]))

    return hand_str

def card_from_card_code(cc):

    card = ""

    # convert value
    if cc[0] == "A":
        card += "ace_of_"
    elif cc[0] == "K":
        card += "king_of_"
    elif cc[0] == "Q":
        card += "queen_of_"
    elif cc[0] == "J":
        card += "jack_of_"
    elif cc[0] == "X":
        card += "10_of_"
    else:
        card += cc[0]
        card += "_of_"

    # convert suit
    if cc[1] == "S":
        card += "spades"
    elif cc[1] == "C":
        card += "clubs"
    elif cc[1] == "H":
        card += "hearts"
    elif cc[1] == "D":
        card += "diamonds"
    else:
        print("Error: card_from_card_code()")

    return card

def dict_from_hand_str(h0, h1, h2, h3):

    card_order = []

    for x in range(0, 13):
        i = x * 2
        card_order.append(card_from_card_code(h0[i:i+2]))
    for x in range(0, 13):
        i = x * 2
        card_order.append(card_from_card_code(h1[i:i+2]))
    for x in range(0, 13):
        i = x * 2
        card_order.append(card_from_card_code(h2[i:i+2]))
    for x in range(0, 13):
        i = x * 2
        card_order.append(card_from_card_code(h3[i:i+2]))

        
    #make_card_html_tags(True, card_order)
    d = create_context_dict(True, card_order)

    return d

def find_hand_with(cc, g):
    '''
    INPUT: CARDCODE cc, GAME g
    OUTPUT: hand 0 1 2 3 which contains card with CARDCODE cc
    '''
    if cc in g.hand_0_initial:
        return 0
    elif cc in g.hand_1_initial:
        return 1
    elif cc in g.hand_2_initial:
        return 2
    elif cc in g.hand_3_initial:
        return 3
    else:
        return -2

def next_hand_from(h):
    if h in [0, 1, 2]:
        return h + 1
    elif h == 3:
        return 0;
    else:
        return -2
