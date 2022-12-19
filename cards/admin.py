from django.contrib import admin
from .models import UserProfile, Deck, Card, DeckImage

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(DeckImage)