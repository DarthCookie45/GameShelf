from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from checkout.utils import user_has_premium

from games.models import Game, PlaySession
from .forms import CustomUserCreationForm

# Create your views here.
# Register view
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# Profile view
@login_required
def profile(request):
    user_games = Game.objects.filter(owner=request.user)

    total_games = user_games.count()
    favourite_games = user_games.filter(favourite=True).count()
    platforms = user_games.values_list('platform', flat=True).distinct()
    platform_count = platforms.count()
    total_play_sessions = PlaySession.objects.filter(game__owner=request.user).count()

    game_type_stats = {}

    for value, label in Game.GAME_TYPE_CHOICES:
        game_type_stats[label] = user_games.filter(game_type=value).count()

    context = {
        'total_games': total_games,
        'favourite_games': favourite_games,
        'platform_count': platform_count,
        'total_play_sessions': total_play_sessions,
        'game_type_stats': game_type_stats,
        'account_tier': 'Premium' if user_has_premium(request.user) else 'Free',
    }

    return render(request, 'accounts/profile.html', context)


# Logout view
@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')

    return redirect('home')