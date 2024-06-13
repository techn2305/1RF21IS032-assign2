# app6/forms.py
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Enter your message")
