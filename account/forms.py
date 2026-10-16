from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Shared base styles
BASE_INPUT = (
    "block w-full rounded-xl border border-slate-300 bg-white "
    "text-slate-900 placeholder-slate-400 shadow-sm "
    "focus:border-brand-500 focus:ring-2 focus:ring-brand-100 focus:outline-none "
    "disabled:bg-slate-50 disabled:text-slate-500 "
    "transition sm:text-sm"
)

# Icon-padded variants (left icon)
INPUT_CLASSES = BASE_INPUT + " pl-10 pr-3 py-2.5"
PASSWORD_CLASSES = BASE_INPUT + " pl-10 pr-10 py-2.5"   # right padding for the eye button

TEXTAREA_CLASSES = BASE_INPUT + " px-3 py-2.5 mt-2 resize-y"

SELECT_CLASSES = (
    "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2.5 "
    "text-slate-900 shadow-sm "
    "focus:border-brand-500 focus:ring-2 focus:ring-brand-100 focus:outline-none "
    "sm:text-sm"
)

FILE_CLASSES = (
    "block w-full text-sm text-slate-900 mt-2 "
    "file:mr-4 file:rounded-lg file:border-0 "
    "file:bg-brand-50 file:px-4 file:py-2 "
    "file:text-sm file:font-semibold file:text-brand-700 "
    "hover:file:bg-brand-100"
)


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter your username",
                "autocomplete": "username",
                "autofocus": True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": PASSWORD_CLASSES,
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
                # Alpine will toggle this dynamically:
                "x-bind:type": "show ? 'text' : 'password'",
            }
        )
    )
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter your username",
                "autocomplete": "username",
                "autofocus": True,
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter your email",
                "autocomplete": "email",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": PASSWORD_CLASSES,
                "placeholder": "Enter your password",
                "autocomplete": "new-password",
                # Alpine will toggle this dynamically:
                "x-bind:type": "show ? 'text' : 'password'",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": PASSWORD_CLASSES,
                "placeholder": "Confirm your password",
                "autocomplete": "new-password",
                # Alpine will toggle this dynamically:
                "x-bind:type": "show ? 'text' : 'password'",
            }
        )
    )