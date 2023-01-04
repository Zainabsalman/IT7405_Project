from django import forms 
from app.models import App

"""
class routerForm(forms.ModelForm):
   class Meta:
     model = App
     fields = '__all__'
      
"""

class routerForm(forms.Form):
   name = forms.CharField()
   description = forms.CharField()
   brand = forms.CharField()
   model = forms.CharField()
   image = forms.FileField()





