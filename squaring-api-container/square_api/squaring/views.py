from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class SquareView(View):
    # logic connecting url to the data that is sending it back
    # only 1 get per class
    # number matches the url number as well, they have to match
    def get(self, request, number):
        return HttpResponse(number**2)

# This Name needs to match on url
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World')
