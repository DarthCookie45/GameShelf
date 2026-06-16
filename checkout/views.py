from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .utils import user_has_premium


# Create your views here.
@login_required
def premium(request):
    has_premium = user_has_premium(request.user)

    context = {
        'has_premium': has_premium,
    }

    return render(request, 'checkout/premium.html', context)