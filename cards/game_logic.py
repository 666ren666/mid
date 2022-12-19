from cards.models import Card
import random


# collect the decks
def collect_decks():
    deck_1 = []
    deck_2 = []
    temp_deck =[]

    all_cards = list(Card.objects.all())
    for card in all_cards:

        if card.deck_id == 1:
            deck_1.append(card)

        if card.deck_id == 2:
            deck_2.append(card)

        if card.deck_id == 3:
            temp_deck.append(card)

    all_decks = [deck_1, deck_2, temp_deck]
    return all_decks


# display amount of cards in deck
def count_cards(deck):
    number_of_cards = 0
    for card in deck:
        number_of_cards +=1
    return number_of_cards


# check if you won or lost the game  
def is_empty(deck_1, deck_2):
    if deck_1 == []:
        return "lose"
    if deck_2 == []:
        return "win"
    else:
        pass


# pull cards and set thier (is_played) field to True
def draw(deck_1, deck_2):

    # find out how many cards are in deck 
    number_of_cards_in_deck_1 = count_cards(deck_1)
    number_of_cards_in_deck_2 = count_cards(deck_2)

    # pick a random number within the number of cards in deck 1
    a = random.randint(0,number_of_cards_in_deck_1-1)
    card_1 = deck_1[a]
    card_1.is_played = True
    card_1.save()

    # pick a random number within the number of cards in deck 2
    b = random.randint(0,number_of_cards_in_deck_2-1)
    card_2 = deck_2[b]
    card_2.is_played = True
    card_2.save()

    return card_1, card_2

# compare cards and asign ids the winning deck 
def greater_than(card_a, card_b, deck_a, deck_b, temp_cards_deck ):

    if card_a.number > card_b.number:
        card_b.deck = card_a.deck
        card_b.save()
        deck_a.append(card_a)
        deck_a.append(card_b)
        if temp_cards_deck  == []:
            pass
        else:
            for card in temp_cards_deck :
                card_x = card
                card_x.deck_id = card_a.deck
                card_x.save()
                deck_a.append(card_x)              


    if card_a.number < card_b.number:
        card_a.deck = card_b.deck
        card_a.save()
        deck_b.append(card_a)
        deck_b.append(card_b)
        if temp_cards_deck  == []:
            pass
        else:
            for card in temp_cards_deck :
                card_y = card
                card_y.deck_id = card_b.deck 
                card_y.save()
                deck_b.append(card_y)            


    if card_a.number == card_b.number:
        card_a.deck_id = '3' 
        card_a.save()
        card_b.deck_id = '3' 
        card_b.save()










# check if all cards in deck were played, and if so - shuffle deck and set all cards (is_played) field to False

# def were_all_cards_played():
#     unplayed_cards_1 = []

#     for card in deck_1:
#         if card.is_played == False:
#             unplayed_cards_1.append(card)    

#             if unplayed_cards_1 != []:
#                 for card in deck_1:
#                     card.is_played = False
#                     card.save()
#             else:
#                 deck_1 = shuffle(deck_1)