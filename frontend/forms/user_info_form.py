from django import forms
from users.models import SEX


class UserInfoForm(forms.Form):
    sex = forms.ChoiceField(label="Sex", choices=SEX)
    # birth_date = forms.DateField(label="Date de naissance", widget=forms.DateField(), required=False)
    first_name = forms.CharField(label='Nom', max_length=100)
    last_name = forms.CharField(label='Prenoms', max_length=100)
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Télephone', max_length=10)
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput, required=True)
