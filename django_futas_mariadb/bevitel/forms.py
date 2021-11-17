from django import forms
from django.forms import fields


##így hozunk létre sima formot
""" class FormName(forms.Form):
    time=forms.CharField()
    distance= forms.FloatField()
    idopont = forms.DateField()
    komment = forms.CharField(widget=forms.Textarea) """

##így hozunk létre model formot:

from statisztika.models import Django_futdb

class NewFutasForm (forms.ModelForm):
    #itt lehetne validálni, ha akarnánk
    class Meta:
        model=Django_futdb
        fields= '__all__'