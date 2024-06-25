# forms.py in search application
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, label='Search for a dish')
