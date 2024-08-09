from django import forms
from services.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name',
            'description',
            'price',
            'price_type',
            'main_image',
            # 'tags',
            'city',
            'address',
            'town'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'main_image': forms.ClearableFileInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(ServiceForm, self).__init__(*args, **kwargs)
    #     self.fields['tags'].required = False
