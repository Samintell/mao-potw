from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Question

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

def active(request):
    now = datetime.now()
    for q in Question.objects.all():
        if (now.day == q.active_date.day) and (now.month == q.active_date.month) and (now.year == q.active_date.year) and (now.hour < 18):
            return render(
                request,
                "proboftheweek/active.html", 
                {
                    'act': True,
                    'act_question': q
                })
    return render(
            request,
            "proboftheweek/active.html", 
            {
                'act': False,
            })




    
