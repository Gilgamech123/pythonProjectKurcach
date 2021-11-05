from django.contrib.auth.models import *
from django import forms
from .models import *


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'passport_data', 'snills']
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = User.objects.latest('id')


class AddDogovor(forms.ModelForm):
    class Meta:
        model = Dogovor
        fields = '__all__'
