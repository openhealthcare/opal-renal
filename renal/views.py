"""
OPAL Renal specific views.
"""
import random

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from opal.models import Episode
from opal.utils.views import LoginRequiredMixin

u = unicode

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


class ReviewSheetView(LoginRequiredMixin, TemplateView):
    """
    Print daily review sheets.
    """
    template_name = 'renal/review_sheet.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ReviewSheetView, self).get_context_data(*args, **kwargs)
        tag, subtag = kwargs.get('tag', None), kwargs.get('subtag', None)
        filter_kwargs = {'active': True}
        if subtag:
            filter_kwargs['tagging__team__name'] = subtag
        elif tag:
            filter_kwargs['tagging__team__name'] = tag
        context['episodes'] = Episode.objects.filter(**filter_kwargs)
        return context

