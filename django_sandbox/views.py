from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def sandbox(request):
    return render(request, 'sandbox.html')


def sandbox_redirect(request):
    return HttpResponseRedirect(reverse('sandbox'))

