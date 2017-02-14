from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Aceasta este aplicatia TEMON</h1>")