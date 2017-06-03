from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label="",
                         required=True,
                         max_length=255,
                         widget=forms.TextInput(attrs={'placeholder': 'Введите url'}))
