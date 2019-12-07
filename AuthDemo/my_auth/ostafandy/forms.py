from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClientUser
from django.contrib.auth.models import User


class SignUpClientForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 characters or fewer.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = ClientUser
        fields = ('full_name', 'email', 'phone_number', 'address_text', 'username', 'password1', 'password2')


class SignUpFormOstafandy(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 characters or fewer.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = ClientUser
        fields = ('full_name', 'email', 'phone_number', 'address_text', 'username',
                  'password1', 'password2', 'craft', 'available_today')
