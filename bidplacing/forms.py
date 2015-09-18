from django.core.exceptions import ValidationError
from django.forms.extras import SelectDateWidget
import datetime
from django import forms
from models import Bid
from models import Product


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = []


class ProductForm(forms.ModelForm):
    initial_date = datetime.date.today() + datetime.timedelta(days=1)
    deadline_time = forms.DateField(widget=SelectDateWidget, initial=initial_date)
    start_price = forms.FloatField(widget=forms.NumberInput(attrs={"step": "0.01"}))

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
            raise ValidationError('Start price must be positive')
        else:
            return price