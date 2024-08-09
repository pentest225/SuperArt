from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    page_redirect = forms.CharField(widget=forms.HiddenInput())
    receiver_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ['content', 'chanel']

        widgets = {
            'chanel': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        labels = {
            'chanel': 'Canal',
            'content': 'Message',
        }

