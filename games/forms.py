from django import forms

from .models import Game


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
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 2:
            raise forms.ValidationError('Please enter a game title.')

        return title

    def clean_platform(self):
        platform = self.cleaned_data['platform'].strip()

        if len(platform) < 2:
            raise forms.ValidationError('Please enter a platform or game format.')

        return platform