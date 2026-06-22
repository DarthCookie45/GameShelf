from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from checkout.utils import user_has_premium

from games.models import Game, PlaySession
from .forms import CustomUserCreationForm, EmailUpdateForm

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
    user_sessions = PlaySession.objects.filter(game__owner=request.user).select_related('game')

    total_games = user_games.count()
    favourite_games = user_games.filter(favourite=True).count()
    platforms = user_games.values_list('platform', flat=True).distinct()
    platform_count = platforms.count()
    total_play_sessions = user_sessions.count()
    has_premium = user_has_premium(request.user)

    game_type_stats = {}

    for value, label in Game.GAME_TYPE_CHOICES:
        game_type_stats[label] = user_games.filter(game_type=value).count()

    format_stats = {}

    for value, label in Game.FORMAT_CHOICES:
        format_stats[label] = user_games.filter(format=value).count()

    ownership_stats = {}

    for value, label in Game.OWNERSHIP_CHOICES:
        ownership_stats[label] = user_games.filter(ownership_status=value).count()

    favourite_percentage = 0

    if total_games > 0:
        favourite_percentage = round((favourite_games / total_games) * 100)

    recent_sessions = user_sessions.order_by('-date_played', '-created_at')[:5]

    most_played_game = None
    most_played_count = 0

    for game in user_games:
        session_count = user_sessions.filter(game=game).count()

        if session_count > most_played_count:
            most_played_game = game
            most_played_count = session_count

    context = {
        'total_games': total_games,
        'favourite_games': favourite_games,
        'platform_count': platform_count,
        'total_play_sessions': total_play_sessions,
        'game_type_stats': game_type_stats,
        'format_stats': format_stats,
        'ownership_stats': ownership_stats,
        'favourite_percentage': favourite_percentage,
        'recent_sessions': recent_sessions,
        'most_played_game': most_played_game,
        'most_played_count': most_played_count,
        'has_premium': has_premium,
        'account_tier': 'Premium' if has_premium else 'Free',
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


#Update email view
@login_required
def edit_email(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Email address updated.')
            return redirect('profile')
    else:
        form = EmailUpdateForm(instance=request.user)

    return render(request, 'accounts/edit_email.html', {'form': form})