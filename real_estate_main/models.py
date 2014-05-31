from django.db import models
from django import newforms as forms
from django.newforms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# Create your models here.

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=Textarea())