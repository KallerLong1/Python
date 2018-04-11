from django.http import HttpResponse 
from django.shortcuts import render

class Model:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def hello(request):
    models = []
    for i in range(0,10):
        modeldata = Model(name = 'Kaller%s'%(i), age = i+20)
        models.append(modeldata)
    context = {}
    context['hello'] = 'Hello World!!'
    context['models'] = models
    return render(request, 'hello.html', context)

def base(request, age):
    context = {}
    context['v'] = 'dasdsa%s'%(age)
    return render(request, 'base.html', context)
