from django.shortcuts import render
from cards.game_logic import count_cards, is_empty, draw, greater_than, collect_decks
from cards.models import DeckImage, UserProfile
from cards.utils import cards_to_decks, make_deck
from cards.leaders import top_players
from cards.forms import LoginForm, SigninForm
from django.contrib import messages 

def main(request):

    background = 'back_ground.jpg'
    global val3
    def val3():
        return background

    profile_pic = 'profile1.png'
    global val4
    def val4():
        return profile_pic

    deck_pic = 'Deck-Red.png'
    global val5
    def val5():
        return deck_pic

    return render(request,'main.html')





def stats(request):
    player = val()
    profile_pic = val4()
    return render(request,'stats.html',{'player':player, 'profile_pic':profile_pic})

def win(request):
    player = val()
    return render(request,'win.html',{'player':player})

def lose(request):
    player = val()
    return render(request,'lose.html',{'player':player})
    
def welcome(request):
    player = UserProfile.objects.get(id=1)
    return render(request,'welcome.html',{'player':player})

def leaderboard(request):
    top_players_list = top_players() 
    return render(request,'leader_board.html',{'top_players':top_players_list})

def game_start(request):
    return render(request,'game_start.html')




def betting(request):
    all_cards = make_deck()
    cards_to_decks(all_cards)
    player = val()
    return render(request,'betting.html', {'player':player})

def betting_20(request):
    player = val()
    bet = 20
    global val2
    def val2():
        return bet
    player.coin = player.coin - bet
    player.save()
    return render(request,'game_start.html', {'player':player})

def betting_50(request):
    player = val()
    bet = 50
    global val2
    def val2():
        return bet
    player.coin = player.coin - bet
    player.save()
    return render(request,'game_start.html', {'player':player})

def betting_100(request):
    player = val()
    bet = 100
    global val2
    def val2():
        return bet
    player.coin = player.coin - bet
    player.save()
    return render(request,'game_start.html',{'player':player})

def betting_200(request):
    player = val()
    bet = 200
    global val2
    def val2():
        return bet
    player.coin = player.coin - bet
    player.save()
    return render(request,'game_start.html',{'player':player})




def game(request):
    player = val()
# set color of deck
    deck_x = DeckImage.objects.get(id=8)
    deck_image = deck_x.image
# collect the decks
    all = collect_decks()
    deck_1 = all[0]
    deck_2 = all[1]
    temp_cards_deck = all[2]
# get amount of cards in each deck 
    amount_1 = int(count_cards(deck_1))
    amount_2 = int(count_cards(deck_2))
# check if either deck is out of cards 

    a = is_empty(deck_1, deck_2)
    if a == "win":
        player = val()
        bet = val2()
        player.coin = player.coin + (bet * 2) 
        player.save()
        return render(request,'win.html',{'player':player})
    if a == "lose":
        return render(request,'lose.html',{'player':player})

# draw a card from each deck 
    card_1, card_2 = draw(deck_1, deck_2)
# compare the cards and update the decks 
    greater_than(card_1, card_2, deck_1, deck_2, temp_cards_deck )

    background = val3()
    profile_pic = val4()
    deck_pic = val5()

    return render(request,'game.html',{'deck_pic':deck_pic, 'profile_pic':profile_pic, 'bg':background,'player':player, 'deck_image':deck_image,'image_1':card_1.image,'image_2':card_2.image,'card_1':card_1, 'card_2':card_2,'amount_1':amount_1, 'amount_2':amount_2})
   



def wrong(request):
    return render(request,'wrong.html')

def pick_game(request):
    return render(request,'pick_game.html')

def under_construction(request):
    return render(request,'under_construction.html')

def war_main(request):
    return render(request,'war_main.html')




def login(request):

    form = LoginForm()
    context = {'form': form}

    if request.method == "GET":
        return render(request,'login.html', context=context)

    else:
        form = LoginForm(request.POST)
        users = list(UserProfile.objects.all())
        name_from_form = form['name'].value()
        password_from_form = form['password'].value()
        
        for user in users:
            if name_from_form == user.name and password_from_form == user.password:
                player_1 = user  
                global val
                def val():
                    return player_1
                return render(request,'welcome.html',{'player':player_1})
        return render(request,"wrong.html")


def signin(request):
    form = SigninForm()
    context = {'form': form}

    if request.method == "GET":
        return render(request,'signin.html', context=context)
        
    else:
        form = SigninForm(request.POST)
        users = list(UserProfile.objects.all())
        name_from_form = form['name'].value()
        
        for user in users:
            if name_from_form == user.name:
                messages.info(request, "User-name is taken, Please try another")
                return render(request,"wrong.html",{'form':form})
            else:
                if form.is_valid():
                    form.save()
                    users = list(UserProfile.objects.all())
                    name_from_form = form['name'].value()
                    password_from_form = form['password'].value()

            for user in users:
                if name_from_form == user.name and password_from_form == user.password:
                    player_1 = user  
                    global val
                    def val():
                        return player_1
                    player_1_id = player_1.id 

                    return render(request,'welcome.html',{'player':player_1, "id":player_1_id})





def options(request):
    background = val3()
    profile_pic = val4()    
    deck_pic = val5()
    return render(request,'options.html',{'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_bg1(request):
    background = 'back_ground.jpg'
    global val3
    def val3():
        return background
    profile_pic = val4()    
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'dedeck_pick': deck_pic})

def option_bg2(request): 
    background = 'back_ground_2.jpg'
    global val3
    def val3():
        return background
    profile_pic = val4()    
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})
     
def option_bg3(request):
    background = 'back ground_3.jpg'
    global val3
    def val3():
        return background   
    profile_pic = val4()    
    deck_pic = val5() 
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})




def option_prof1(request):
    profile_pic = 'profile1.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_prof2(request):
    profile_pic = 'profile2.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_prof3(request):
    profile_pic = 'profile3.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_prof4(request):
    profile_pic = 'profile4.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_prof5(request):
    profile_pic = 'profile5.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_prof6(request):
    profile_pic = 'profile6.png'
    global val4
    def val4():
        return profile_pic
    background = val3()
    deck_pic = val5()
    return render(request,'options.html', {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})



def option_deck1(request):
    deck_pic = 'Deck-Red.png'
    global val5
    def val5():
        return deck_pic   
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})
def option_deck2(request):
    deck_pic = 'Deck-Purple.png'
    global val5
    def val5():
        return deck_pic  
    profile_pic = val4() 
    background = val3()  
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_deck3(request):
    deck_pic = 'Deck-Blue.png'
    global val5
    def val5():
        return deck_pic  
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_deck4(request):
    deck_pic = 'Deck-Green.png'
    global val5
    def val5():
        return deck_pic    
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_deck5(request):
    deck_pic = 'Deck-Yellow.png'
    global val5
    def val5():
        return deck_pic    
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_deck6(request):
    deck_pic = 'Deck-Orange.png'
    global val5
    def val5():
        return deck_pic 
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})

def option_deck7(request):
    deck_pic = 'Deck-Grey.png'
    global val5
    def val5():
        return deck_pic  
    profile_pic = val4() 
    background = val3()
    return render(request,'options.html',  {'bg': background,'profile_pic':profile_pic,'deck_pic': deck_pic})