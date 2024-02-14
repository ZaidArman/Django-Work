from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, required=True, label="Password", widget=forms.TextInput(attrs={'class':'form-control'}))
    
class SignUp(forms.Form):
    fullname = forms.CharField(max_length=100, required=True, label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100, required=True, label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, required=True, label="Password", widget=forms.TextInput(attrs={'class':'form-control'}))
    