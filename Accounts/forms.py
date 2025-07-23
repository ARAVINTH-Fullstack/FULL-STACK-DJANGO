from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'type':'text',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'type':'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
            'id':'inputBox1',
            'type':'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
            'id':'inputBox2',
            'type':'password',
        })

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile','address','city','country','pin_code']