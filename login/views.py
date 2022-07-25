from django.apps import apps
from django.http import HttpResponse
from django.template import loader
from befor90.views import indexb

def index(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

def add(request):
  indexb(request)