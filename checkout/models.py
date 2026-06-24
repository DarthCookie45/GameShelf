from django.conf import settings
from django.db import models


# Create your models here.
class PremiumAccess(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='premium_access',
    )
    paid = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=255, blank=True)
    accent_colour = models.CharField(max_length=20, default='matcha-mist')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'premium access records'

    def __str__(self):
        status = 'Premium' if self.paid else 'Free'
        return f'{self.user.username} - {status}'
