from django.shortcuts import render, HttpResponse, reverse

def index(request):
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href=\"/rango/\">Index</a>")