from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import GameForm
from .models import Game

# Create your views here.
def get_sort_url(current_sort, field_name):
    if current_sort == field_name:
        return f'-{field_name}'

    return field_name


@login_required
def games_list(request):
    games = Game.objects.filter(owner=request.user)

    search_query = request.GET.get('q', '').strip()
    game_type = request.GET.get('game_type', '')
    ownership_status = request.GET.get('ownership_status', '')
    game_format = request.GET.get('format', '')
    favourite = request.GET.get('favourite', '')
    sort = request.GET.get('sort', 'title')

    if search_query:
        games = games.filter(
            Q(title__icontains=search_query)
            | Q(platform__icontains=search_query)
            | Q(genre__icontains=search_query)
        )

    if game_type:
        games = games.filter(game_type=game_type)

    if ownership_status:
        games = games.filter(ownership_status=ownership_status)

    if game_format:
        games = games.filter(format=game_format)

    if favourite == 'on':
        games = games.filter(favourite=True)

    allowed_sorts = [
        'title',
        '-title',
        'game_type',
        '-game_type',
        'platform',
        '-platform',
        'ownership_status',
        '-ownership_status',
        'format',
        '-format',
        'purchase_date',
        '-purchase_date',
    ]

    if sort not in allowed_sorts:
        sort = 'title'

    games = games.order_by(sort)

    context = {
        'games': games,
        'search_query': search_query,
        'selected_game_type': game_type,
        'selected_ownership_status': ownership_status,
        'selected_format': game_format,
        'selected_favourite': favourite,
        'current_sort': sort,
        'game_type_choices': Game.GAME_TYPE_CHOICES,
        'ownership_choices': Game.OWNERSHIP_CHOICES,
        'format_choices': Game.FORMAT_CHOICES,
        'title_sort': get_sort_url(sort, 'title'),
        'type_sort': get_sort_url(sort, 'game_type'),
        'platform_sort': get_sort_url(sort, 'platform'),
        'ownership_sort': get_sort_url(sort, 'ownership_status'),
        'format_sort': get_sort_url(sort, 'format'),
        'purchase_sort': get_sort_url(sort, 'purchase_date'),
    }

    return render(request, 'games/games_list.html', context)


@login_required
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)

        if form.is_valid():
            game = form.save(commit=False)
            game.owner = request.user
            game.save()

            messages.success(request, 'Game added to your shelf.')
            return redirect('games_list')
    else:
        form = GameForm()

    return render(request, 'games/game_form.html', {'form': form, 'page_title': 'Add Game'})