from django import forms
from .models import Meep
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# create a Meep from
class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   'placeholder': 'Enter Your Musker Meep',
                                   'class': 'form-control'
                               },
                           ),
                           label=''
                           )

    class Meta:
        model = Meep
        fields = ('body',)
        # exclude=('user',)


class SigninForm(UserCreationForm):
    # username = forms.CharField(label='', max_length=50,
    #                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}),
    #                            required=True)
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False)

    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                required=False)
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
                             required=False)

    # password1 = forms.CharField(label='',
    #                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Conform Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateUser(UserChangeForm):
    password = None
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email=forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        # self.fields['first_name'].label = ''
        # self.fields[
        #     'first_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
