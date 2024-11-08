from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control p-3', 'placeholder': 'Email' }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control p-3', 'placeholder': 'Password'}))
    conForm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control p-3', 'placeholder': 'Confirm Password'}))
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control p-3', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control p-3', 'placeholder': 'Password'}))