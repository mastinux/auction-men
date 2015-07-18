__author__ = 'neuro'

from django import forms
from django.contrib.auth.models import User, AbstractUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AbstractUser
        fields = ['username', 'email', 'password']



    def clean_username(self):
        username = self.cleaned_data['username']
        print username
        return username

    #def clean_email(self):
    #   email = self.cleaned_data
    #    print email
    #    return email



