from django import forms

class LetterForm(forms.Form):
    letter = forms.CharField(label='Your letter content', max_length=200)
    author = forms.CharField(label='Your name', max_length=30)