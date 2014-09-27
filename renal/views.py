"""
eLCID specific views.
"""
import csv
import random

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, View
import letter
from letter.contrib.contact import EmailForm, EmailView

from opal.views import ReportView


u = unicode
POSTIE = letter.DjangoPostman()

def temp_password():
    num = random.randint(1, 100)
    word = random.choice(['womble', 'bananas', 'flabbergasted', 'kerfuffle'])
    return '{0}{1}'.format(num, word)


class Error500View(View):
    """
    Demonstrative 500 error to preview templates.
    """
    def get(self, *args, **kwargs):
        if self.request.META['HTTP_USER_AGENT'].find('Googlebot') != -1:
            return HttpResponse('No')
        raise Exception("This is a deliberate error")
