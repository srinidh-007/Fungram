from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def validateEmail( self,email ):
    
        from django.core.exceptions import ValidationError
        try:
            validate_email( email )
            return True
        except ValidationError:
            return False

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']