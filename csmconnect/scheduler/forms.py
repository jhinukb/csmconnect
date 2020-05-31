from django import forms

class SignUpForm(forms.Form):
    your_name = forms.CharField(label='Your name:', max_length=100)
    your_email = forms.EmailField(label='Your email:')
    password = forms.CharField(label='Enter password:', widget=forms.PasswordInput, min_length=8, max_length=32)
    #Note: Can add confirm password field later.
    account_type = forms.ChoiceField(label='Choose account type:', choices=[('M', 'Mentor'), ('S', 'Student')])

class LoginForm(forms.Form):
    your_email = forms.EmailField(label='Your email:')
    password = forms.CharField(label='Enter password:', widget=forms.PasswordInput, min_length=8, max_length=32)
