from django.db import models

# Create your models here.
class Game(models.Model):
    '''
    trick_number : 1 - 13
    initial hands
    cards played by round
    '''

    game_num = models.IntegerField(default=0)

    date_played = models.DateField(null=True)

    # "2C,3H,4S,5D,...,6H"
    hand_0_initial = models.CharField(max_length=26, default="0")
    hand_1_initial = models.CharField(max_length=26, default="0")
    hand_2_initial = models.CharField(max_length=26, default="0")
    hand_3_initial = models.CharField(max_length=26, default="0")

    # 1 - 13
    trick_number = models.IntegerField(default=0)

    # 0 - 3
    trick_winner = models.IntegerField(default=-1)

    # true : hearts has been played
    hearts_played = models.BooleanField(default=False)

    # "S,H0,H1,H2,H3,W"
    # S : which hand started
    # H0 : denotes which card was played by H0
    # W : which hand was the winner of the trick
    '''
    trick_1 = models.CharField(max_length=13)
    trick_2 = models.CharField(max_length=13)
    trick_3 = models.CharField(max_length=13)
    trick_4 = models.CharField(max_length=13)
    trick_5 = models.CharField(max_length=13)
    trick_6 = models.CharField(max_length=13)
    trick_7 = models.CharField(max_length=13)
    trick_8 = models.CharField(max_length=13)
    trick_9 = models.CharField(max_length=13)
    trick_10 = models.CharField(max_length=13)
    trick_11 = models.CharField(max_length=13)
    trick_12 = models.CharField(max_length=13)
    trick_13 = models.CharField(max_length=13)
    '''
    trick_history = models.CharField(max_length=117, default="")
