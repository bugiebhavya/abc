from django import forms

from .models import Item
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('user','name','brand','category','price', 'quantity','total_price')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'brand': forms.TextInput(attrs={'class': 'textinputclass'}),
            'price': forms.TextInput(attrs={'class': 'textinputclass'}),
            'quantity': forms.TextInput(attrs={'class': 'textinputclass'}),
        }
