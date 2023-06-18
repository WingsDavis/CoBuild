from . models import Project
from django.forms import ModelForm
from django import forms

class CreateSpace(ModelForm):
    
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['admin' , 'followers']
