from django.core.exceptions import ValidationError
from django.forms.extras import SelectDateWidget
import datetime

__author__ = 'mastinux'

from django import forms
from models import Bid
from models import Product


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = []

class ProductForm(forms.ModelForm):
    deadline_time = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Product
        exclude = ['seller']

    def clean_deadline_time(self):
        deadline = self.cleaned_data['deadline_time']
        today = datetime.datetime.today().date()
        if deadline <= today:
            raise ValidationError('deadline must be a future date')
        else:
            return deadline


    def clean_start_price(self):
        price = self.cleaned_data['start_price']
        if price < 0:
            raise ValidationError('Start price must ne positive')
        else:
            return price
