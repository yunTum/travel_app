from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Card)
class Card(admin.ModelAdmin):
    pass

@admin.register(PlaceName)
class PlaceName(admin.ModelAdmin):
    pass

@admin.register(CardToCard)
class CardToCard(admin.ModelAdmin):
    pass

