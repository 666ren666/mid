# from cards.forms import LoginForm, SigninForm
# from cards.models import UserProfile


# def whom_is_playing():

#     form_a = LoginForm()
#     form_b = SigninForm()

#     users = list(UserProfile.objects.all())
#     name_form_a = form_a['name'].value()
#     password_form_a = form_a['password'].value()
#     name_form_b = form_b['name'].value()
#     password_form_b = form_b['password'].value()
    
#     for user in users:
#         if name_form_a == user.name and password_form_a == user.password:
#             player_1 = user  
#             print(player_1)
#             return player_1

#         if name_form_b == user.name and password_form_b == user.password :
#             player_1 = user 
#             print(player_1)

#             return player_1

#         else:
#             player_1 = "xxxxxxxxx"