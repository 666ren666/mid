from django.contrib import admin
from django.urls import path
from cards import views


app_name = 'cards'
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.main, name="main"),

    path('login', views.login, name="login"),
    path('signin', views.signin, name="signin"),
        path('wrong', views.wrong, name="wrong"),
        path('welcome', views.welcome, name="welcome"),

    path('pick_game', views.pick_game, name="pick_game"),
        path('war_main', views.war_main, name="war_main"),
        path('under_construction', views.under_construction, name="under_construction"),

    path('betting', views.betting, name="betting"),
        path('betting_20', views.betting_20, name="betting_20"),
        path('betting_50', views.betting_50, name="betting_50"),
        path('betting_100', views.betting_100, name="betting_100"),
        path('betting_200', views.betting_200, name="betting_200"),
            path('game_start', views.game_start, name="game_start"),

    path('game', views.game, name="game"),
        path('win', views.win, name="win"),
        path('lose', views.lose, name="lose"),
        
        path('stats', views.stats, name="stats"),
        path('options', views.options, name="options"),
            path('option_bg1', views.option_bg1, name="option_bg1"),
            path('option_bg2', views.option_bg2, name="option_bg2"),
            path('option_bg3', views.option_bg3, name="option_bg3"),

            path('option_prof1', views.option_prof1, name="option_prof1"),
            path('option_prof2', views.option_prof2, name="option_prof2"),
            path('option_prof3', views.option_prof3, name="option_prof3"),
            path('option_prof4', views.option_prof4, name="option_prof4"),
            path('option_prof5', views.option_prof5, name="option_prof5"),
            path('option_prof6', views.option_prof6, name="option_prof6"),

            path('option_deck1', views.option_deck1, name="option_deck1"),
            path('option_deck2', views.option_deck2, name="option_deck2"),
            path('option_deck3', views.option_deck3, name="option_deck3"),
            path('option_deck4', views.option_deck4, name="option_deck4"),
            path('option_deck5', views.option_deck5, name="option_deck5"),
            path('option_deck6', views.option_deck6, name="option_deck6"),
            path('option_deck7', views.option_deck7, name="option_deck7"),

    path('leaderboard', views.leaderboard, name="leaderboard"),
]