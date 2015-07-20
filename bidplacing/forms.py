__author__ = 'mastinux'

from django import forms


class AmountForm(forms.Form):
    amount = forms.CharField()