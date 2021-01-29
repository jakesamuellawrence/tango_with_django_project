from django.shortcuts import render, HttpResponse, reverse

def index(request):
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context)

def about(request):
    return render(request, 'rango/about.html', context={})