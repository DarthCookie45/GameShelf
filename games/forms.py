from django import forms

from .models import Game, PlaySession


class GameImageWidget(forms.ClearableFileInput):
    template_name = 'widgets/game_image_widget.html'


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'game_type',
            'platform',
            'ownership_status',
            'format',
            'genre',
            'player_count',
            'purchase_date',
            'favourite',
            'image',
            'notes',
        ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            'image': GameImageWidget(),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 2:
            raise forms.ValidationError('Please enter a game title.')

        return title

    def clean_platform(self):
        platform = self.cleaned_data['platform'].strip()

        if len(platform) < 2:
            raise forms.ValidationError(
                'Please enter a platform or game format.'
            )

        return platform

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'e.g. UNO, Pokemon, God of War'
        })

        self.fields['platform'].widget.attrs.update({
            'placeholder': 'e.g. PS5, PC, Nintendo Switch'
        })

        self.fields['genre'].widget.attrs.update({
            'placeholder': 'e.g. RPG, strategy, party game'
        })

        self.fields['player_count'].widget.attrs.update({
            'placeholder': 'e.g. 1-4 players'
        })

        self.fields['notes'].widget.attrs.update({
            'placeholder':
                'Add condition, edition, DLC, house rules or extra notes here',
            'rows': 5
        })


class PlaySessionForm(forms.ModelForm):
    class Meta:
        model = PlaySession
        fields = [
            'date_played', 'players', 'winner', 'result_summary', 'notes'
        ]
        widgets = {
            'date_played': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_players(self):
        players = self.cleaned_data['players'].strip()

        if len(players) < 2:
            raise forms.ValidationError('Please enter at least one player.')

        return players
