from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=20, default='name')
    age = models.CharField(max_length=20, null=False, default=666)
    coin = models.IntegerField(null=False, default=1000)
    image = models.ImageField(null=True, blank=True, default='profile2.png')
    password = models.CharField(max_length=20, default='password')

    def __str__(self):
        return f'{self.name} has {self.coin} coins'

class Deck(models.Model):
    deck_name = models.CharField(max_length=100,default="deck_player_name")
    amount_of_cards = models.IntegerField(null=False, default=52)
    
    def __str__(self):
        return f'{self.deck_name} has {self.amount_of_cards} cards in his/her deck'



class Card(models.Model):
    CLUBS, DIAMONDS, HEARTS, SPADES = 1, 2, 3, 4
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

    SUITS = ((CLUBS, 'CLUBS'), (DIAMONDS, 'DIAMONDS'), (HEARTS, 'HEARTS'), (SPADES, 'SPADES'),)
    NUMBERS = ((TWO,'2'),(THREE, '3'),(FOUR, '4'),(FIVE, '5'),(SIX, '6'),(SEVEN, '7'),(EIGHT, '8'),(NINE, '9'),(TEN, '10'),(JACK, 'J'),(QUEEN, 'Q'),(KING, 'K'),(ACE, 'A'),)

    suit = models.PositiveSmallIntegerField(choices=SUITS)
    number = models.PositiveSmallIntegerField(choices=NUMBERS)
    image = models.ImageField(null=True, blank=True, default='B-Red.png')
    deck = models.ForeignKey(Deck, null=True, on_delete=models.DO_NOTHING)
    is_played = models.BooleanField(default=False)

    def __str__(self):
        typed_suit = self.get_suit_display()
        typed_number = self.get_number_display()
        return f'{typed_number} of {typed_suit} {self.image}'

class DeckImage(models.Model):
    name = models.CharField(max_length=20, default="Red")
    image = models.ImageField(null=True, blank=True, default='B-Red.png')

    def __str__(self):
        return self.name
