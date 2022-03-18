from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the main page for the Kenilworth Election Results database.")