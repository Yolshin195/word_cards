from django import forms
from .models import WordCard
from django.utils.translation import gettext_lazy as _


class WordCardFilterForm(forms.Form):
    front = forms.CharField(
        label=_('Front'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter front text')}),
        required=True
    )


class WordCardForm(forms.ModelForm):
    class Meta:
        model = WordCard
        fields = ['front', 'back']
        widgets = {
            'front': forms.TextInput(attrs={'class': 'form-control'}),
            'back': forms.TextInput(attrs={'class': 'form-control'}),
        }
