from django.shortcuts import render
from .models import Artiles
from django.db.models import Sum, Avg
from django.views.generic import UpdateView
from .forms import *


def index(request):
    ind = Artiles.objects.all()
    t0 = ind[0].tittle
    t1 = ind[1].tittle
    t2 = ind[2].tittle
    mo0 = ind[0].mod
    mo1 = ind[1].mod
    mo2 = ind[2].mod
    v0 = ind[0].ves
    v1 = ind[1].ves
    v2 = ind[2].ves
    m0 = ind[0].maxg
    m1 = ind[1].maxg
    m2 = ind[2].maxg
    ras0 = (m0/v0)*100
    ras1 = (m1/v1)*100
    ras2 = (m2/v2)*100
    p0 = 100 - ras0
    p1 = 100 - ras1
    p2 = 100 - ras2
    if p0 < 0:
        p0 = 0
        if p1 < 0:
            p0 = 0
            if p2 < 0:
                p0 = 0
    data = {
        'ind': ind, 't0': t0, 't1': t1, 't2': t2, 'mo0': mo0, 'mo1': mo1, 'mo2': mo2, 'v0': v0, 'v1': v1, 'v2': v2, 'm0': m0, 'm1': m1, 'm2': m2, 'p0': p0, 'p1': p1, 'p2': p2,
    }
    return render(request, 'main/index.html', data)


def vse(request):
    vs = Artiles.objects.aggregate(Sum('ves'))
    fer = Artiles.objects.aggregate(Avg('FE'))
    si = Artiles.objects.aggregate(Avg('SiO2'))
    return render(request, 'main/test.html', {'vs': vs, 'fer': fer, 'si': si})


def test(request):
    a = Artiles.objects.all()
    inp0 = [1, 1]
    inp1 = [1, 2]
    inp2 = [1, 3]
    ves0 = a[0].ves
    ves1 = a[1].ves
    ves2 = a[2].ves
    wkt = [1, 1], [1, 2], [1, 3], [1, 4]
    for el in wkt:
        if el == inp0:
            ves0 = a[0].ves
        else:
            ves0 = 0
        if el == inp1:
            ves1 = a[1].ves
        else:
            ves1 = 0
            if el == inp2:
                ves2 = a[2].ves
            else:
                ves2 = 0
    res = ves0 + ves1 + ves2
    return render(request, 'main/fun.html',  {'res': res})





# from main.models import Artiles

