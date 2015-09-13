from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#  created by Eric but then removed 

# Hello World test
# from django.http import HttpResponse
# def TestView(request, **kwargs):
#     return HttpResponse("Hello World!")

class SplashView(TemplateView):
	template_name = 'index.html'