from .utils import user_has_premium


def premium_status(request):
    return {
        'has_premium': user_has_premium(request.user),
    }