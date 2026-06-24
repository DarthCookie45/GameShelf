from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Used for password reset.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account already exists with this email address.'
            )

        return email


class EmailUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email_exists = User.objects.filter(
                email__iexact=email
            ).exclude(
                pk=self.instance.pk
            ).exists()

            if email_exists:
                raise forms.ValidationError(
                    'An account already exists with this email address.'
                )

        return email
