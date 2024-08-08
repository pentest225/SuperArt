from django import forms
from users.models import Artisan


# class ArtisanForm(forms.ModelForm):
#     class Meta:
#         model = Artisan
#         fields = [
#             'birth_date', 'profile_image', 'sectors', 'bio',
#             'sex', 'city', 'location_lat', 'location_lon', 'study_level',
#             'phone_number', 'whatsApp_phone',
#         ]
#
#         labels = {
#             'birth_date': 'Date de naissance',
#             'profile_image': 'Profil image',
#             'sectors': "Secteur d'activité",
#             'bio': 'Biographie',
#             'city': 'Ville',
#             'location_lat': 'Latitude',
#             'location_lon': 'Longitude',
#             'study_level': "Niveau d'étude",
#             'whatsApp_phone': 'Numéro WhatsApp',
#         }
#         sector_choice = [(1, 'Menuiserie'), (2, 'Plomberie'), (3, 'Électricité'), (4, 'Maçonnerie')]
#
#         widgets = {
#             'sectors': forms.Select(attrs={'placeholder': "Selectionez au moins un secteur d'activité"},choices=sector_choice),  # Widget pour sélection multiple
#         }
