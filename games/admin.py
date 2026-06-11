from django.contrib import admin

from .models import Game

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'owner',
        'game_type',
        'platform',
        'ownership_status',
        'favourite',
    )
    list_filter = (
        'game_type',
        'ownership_status',
        'format',
        'favourite',
    )
    search_fields = ('title', 'platform', 'genre', 'owner__username')