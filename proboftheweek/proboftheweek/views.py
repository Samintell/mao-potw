from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()

    html_content = "<html><head><title>Hello, Django</title></head><body>"
    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"
    

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
        "proboftheweek/layout.html", 
        {
            
        })
