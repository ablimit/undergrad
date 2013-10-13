from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
# from django.core.context_processors import csrf


def home(request):
    t = get_template('index.html')
    homepage= t.render(Context())
    return HttpResponse(homepage)

