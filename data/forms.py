from django import forms
from data.models import Data

class AddDataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('name','parent',)