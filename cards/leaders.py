from cards.models import UserProfile


def top_players():
    top_players = []
    ordered_players = list(UserProfile.objects.all().order_by('-coin'))

    i = 0
    while i < 10:
        top_players.append(ordered_players.pop(0))
        i += 1

    return top_players
