from django.contrib import admin

from .models import PremiumAccess

# Register your models here.
@admin.register(PremiumAccess)
class PremiumAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid', 'created_at')
    search_fields = ('user__username', 'stripe_checkout_id')
    list_filter = ('paid',)