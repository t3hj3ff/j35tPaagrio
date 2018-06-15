from django import forms

class paygol(forms.Form):
    pg_price = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
