from .models import PremiumAccess


def user_has_premium(user):
    if not user.is_authenticated:
        return False

    return PremiumAccess.objects.filter(user=user, paid=True).exists()
