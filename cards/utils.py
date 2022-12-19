import random
from cards.models import Card, Deck


# create cards table
def create_deck():
    suits = [1, 2, 3, 4]
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    cards = [Card(suit=suit, number=number, image=image_connection(number, suit)) for number in numbers for suit in suits]
    Card.objects.bulk_create(cards)

def image_connection(number, suit):

    if suit == 1:
        suit = "C"
    if suit == 2:
        suit = "D"
    if suit == 3:
        suit = "H"
    if suit == 4:
        suit = "S"

    if number == '2':
        number = "2"
    if number == '3':
        number = "3"
    if number == '4':
        number = "4"
    if number == '5':
        number = "5"
    if number == '6':
        number = "6"
    if number == '7':
        number = "7"
    if number == '8':
        number = "8"
    if number == '9':
        number = "9"
    if number == '10':
        number = "10"
    if number == '11':
        number = "J"
    if number == '12':
        number = "Q"
    if number == '13':
        number = "K"
    if number == '14':
        number = "A"


    a = str(f"{number}-{suit}.png")
    image = a
    return image

# # shuffle and deal cards to 2 seprate decks 

def make_deck():
    from cards.models import Card
    card_list = list(Card.objects.all())
    random.shuffle(card_list)
    return card_list

def cards_to_decks(card_list):
    deck1 = Deck.objects.get(id=1)
    deck2 = Deck.objects.get(id=2)
    
    for count, card in enumerate(card_list):
            if count % 2 == 0:
                card.deck = deck1
            else:
                card.deck = deck2
            card.save()


    # counter = 1
    # for card in card_list:
    #     if counter % 2 == 0:
    #         card.deck = deck1
    #         counter += 1 
    #     else:
    #         card.deck = deck2
    #         counter += 1 
    #     card.save()

