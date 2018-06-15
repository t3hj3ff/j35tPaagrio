from django import forms
from master_account.models import Accounts
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

currentuser = get_user_model()

class ChildUser(forms.ModelForm):
    password_confirm = forms.CharField(max_length=20, required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ChildUser, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ChildUser, self).clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
            if len(password) < 6:
                raise forms.ValidationError("Password must be @least 6 characters long")
        return cleaned_data

    class Meta:
        model = Accounts
        fields = ["login","password","password_confirm"]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class':'form-control'}),
            'password_confirm': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


    def clean_password(self):
        cleaned_data = super(ChildUser, self).clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
            if len(password) < 6:
                raise forms.ValidationError("Password must be @least 6 characters long")
        return password

class ChildUserPasswordChange(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChildUserPasswordChange, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ChildUserPasswordChange, self).clean()

        password = cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("Password must be @least 6 characters long")
        return cleaned_data

    class Meta:
        model = Accounts
        fields = ['password']
        exclude = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'password': 'Category Name',
        }
        error_messages = {
            'password': {
                'required': ("Password must not be less than 6 Characters."),
            },
        }
    def clean_password(self):
        cleaned_data = super(ChildUserPasswordChange, self).clean()
        password = cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("Your password should be at least 6 Characters")

        return password


class TransferFunds(forms.Form):
    amount = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))

class TransferBonus(forms.Form):
    amount = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
