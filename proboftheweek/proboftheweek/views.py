from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            'title': 'testme',
            'message': 'sanity check'
        })

def test(request):
    now = datetime.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            
        })
