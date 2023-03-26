from django import forms
from .models import Item


class CaptureForm(forms.Form):
    description = forms.CharField(label='stuff description', max_length=256)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'form-control col-9'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter text'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write something about "stuff"'}),
        }
