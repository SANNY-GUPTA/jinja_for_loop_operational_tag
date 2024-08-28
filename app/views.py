from django.shortcuts import render

def loop(request):
    d={'a':100,'name':'sanny','n':'123456789'}
    return render(request,'loop.html',d)