import datetime

from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
def index(request):
    date_jour = datetime.now()
    #html = "<html><body>Il est %s.</body></html>" % date_jour
    #html = f'<html><body>Il est {date_jour}.</body></html>'
    #return HttpResponse(html)
    VAR={
            'date':date_jour,
            'pseudo': 'Tom Tom'
        }
    return render(
        request,
        'catalog/index.html',
        context=VAR
    )