from django import forms


class SearchForm(forms.Form):
    user_rating_min = forms.CharField(label='Minimal user rating')
