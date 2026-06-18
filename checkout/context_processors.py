from .utils import user_has_premium


def premium_status(request):
    has_premium = False
    accent_colour = 'matcha-mist'

    if request.user.is_authenticated:
        premium_access = getattr(request.user, 'premium_access', None)

        if premium_access and premium_access.paid:
            has_premium = True
            accent_colour = premium_access.accent_colour

    return {
        'has_premium': has_premium,
        'accent_colour': accent_colour,
    }