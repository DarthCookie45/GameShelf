import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import PremiumAccess
from .utils import user_has_premium


# Create your views here.
@login_required
def premium(request):
    has_premium = user_has_premium(request.user)

    context = {
        'has_premium': has_premium,
    }

    return render(request, 'checkout/premium.html', context)


@login_required
def create_checkout_session(request):
    if request.method != 'POST':
        return redirect('premium')

    if user_has_premium(request.user):
        messages.info(request, 'Premium is already unlocked.')
        return redirect('premium')

    if not settings.STRIPE_SECRET_KEY:
        messages.error(request, 'Stripe is not configured yet.')
        return redirect('premium')

    stripe.api_key = settings.STRIPE_SECRET_KEY

    success_url = request.build_absolute_uri(reverse('payment_success'))
    cancel_url = request.build_absolute_uri(reverse('payment_cancel'))

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        line_items=[
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': 'GameShelf Premium',
                    },
                    'unit_amount': settings.STRIPE_PREMIUM_PRICE,
                },
                'quantity': 1,
            }
        ],
        success_url=f'{success_url}?session_id={{CHECKOUT_SESSION_ID}}',
        cancel_url=cancel_url,
        customer_email=request.user.email or None,
    )

    return redirect(session.url)


@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')

    if not session_id or not settings.STRIPE_SECRET_KEY:
        messages.error(request, 'Payment could not be verified.')
        return redirect('premium')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status == 'paid':
        PremiumAccess.objects.update_or_create(
            user=request.user,
            defaults={
                'paid': True,
                'stripe_checkout_id': session_id,
            },
        )
        messages.success(request, 'Payment successful. Premium unlocked.')
    else:
        messages.error(request, 'Payment was not completed.')

    return redirect('premium')


@login_required
def payment_cancel(request):
    messages.warning(request, 'Payment cancelled. You have not been charged.')
    return redirect('premium')