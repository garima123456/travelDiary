from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
   context_dict = {'boldmessage': "This is website to find the places to chill "}
   return render(request, 'food/index2.html', context_dict)
