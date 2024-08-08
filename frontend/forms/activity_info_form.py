from django import forms


class ActivityInfoForm(forms.Form):
    profile_image = forms.ImageField(label='Image de profile')
    sectors = forms.ChoiceField(label="Secteur d'activité", widget=forms.Select(
        attrs={'class': 'chosen-select', 'placeholder': "Selectionez au moins un secteur d'activité"}))
    bio = forms.CharField(label="Biographie", widget=forms.Textarea)
    whatsApp_phone = forms.CharField(label="WhatsApp phone", max_length=10)
