from django import forms
from .models import Meep


# create a Meep from
class MeepForm(forms.ModelForm):
    body=forms.CharField(required=True,
            widget=forms.widgets.Textarea(
                attrs={
                    'placeholder':'Enter Your Musker Meep',
                    'class':'form-control'
                },
            ),
            label=''
           )
    class Meta:
        model = Meep
        fields = ('body',)
        # exclude=('user',)
