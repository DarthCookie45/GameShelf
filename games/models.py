from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    BOARD_GAME = 'board_game'
    CARD_GAME = 'card_game'
    TABLETOP_GAME = 'tabletop_game'
    VIDEO_GAME = 'video_game'

    GAME_TYPE_CHOICES = [
        (BOARD_GAME, 'Board game'),
        (CARD_GAME, 'Card game'),
        (TABLETOP_GAME, 'Tabletop game'),
        (VIDEO_GAME, 'Video game'),
    ]

    OWNED = 'owned'
    WISHLIST = 'wishlist'
    BORROWED = 'borrowed'
    SOLD = 'sold'

    OWNERSHIP_CHOICES = [
        (OWNED, 'Owned'),
        (WISHLIST, 'Wishlist'),
        (BORROWED, 'Borrowed'),
        (SOLD, 'Sold'),
    ]

    PHYSICAL = 'physical'
    DIGITAL = 'digital'
    SUBSCRIPTION = 'subscription'

    FORMAT_CHOICES = [
        (PHYSICAL, 'Physical'),
        (DIGITAL, 'Digital'),
        (SUBSCRIPTION, 'Subscription'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='games',
    )
    title = models.CharField(max_length=120)
    game_type = models.CharField(max_length=30, choices=GAME_TYPE_CHOICES)
    platform = models.CharField(max_length=80)
    ownership_status = models.CharField(
        max_length=30,
        choices=OWNERSHIP_CHOICES,
        default=OWNED,
    )
    format = models.CharField(
        max_length=30,
        choices=FORMAT_CHOICES,
        default=PHYSICAL,
    )
    genre = models.CharField(max_length=80, blank=True)
    player_count = models.CharField(max_length=40, blank=True)
    purchase_date = models.DateField(blank=True, null=True)
    favourite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='game_images/', blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk': self.pk})