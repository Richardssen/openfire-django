'''
Created on Apr 29, 2015

@author: nishant.nawarkhede
'''
from django import  forms

class EditUser(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    
class CreateNewUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField()
    email = forms.EmailField()
    
class AddFriend(forms.Form):
    username = forms.CharField()
    friendname =  forms.CharField()
    