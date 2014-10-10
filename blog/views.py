# -*- coding: utf-8 -*-

from django.shortcuts import render
from datetime import datetime
# Create your views here.



from django.http import HttpResponse


def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def tpl(request):
    return render(request, 'blog/tpl.html', {'utc_date': datetime.utcnow,
                                             'current_date': datetime.now,
                                            })


def addition(request, nombre1, nombre2, nom="André", age = "28"):
    total = int(nombre1) + int(nombre2)

    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())

