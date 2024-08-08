from django import forms
from django.forms import ModelForm
from django import forms

from users.models import Artisan


class ArtisanForm(ModelForm):
    class Meta:
        model = Artisan
        fields = ('profile_image', 'sectors', 'bio', 'sex', 'city')


FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black")
]



class FirstForm(forms.Form):

    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    CHOICES = [
        ("1", "First"),
        ("2", "Second")
    ]
    subject = forms.CharField(label='Sujet', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label='Email')
    cc_myself = forms.BooleanField(required=False)
    birth_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'placeholder': 'Select color'}),
        choices=FAVORITE_COLORS_CHOICES,
    )
    radio = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'display-inline'}), choices=CHOICES)


# class UserInfoForm(ModelForm):
#     class Meta:
#         model = Artisan
#         fields = ('sex', 'first_name', 'last_name', 'email', 'birth_date', 'phone_number')
