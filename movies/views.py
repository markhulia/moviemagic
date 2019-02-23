from django.http import HttpResponse


def index(request):
    return HttpResponse("Let's do this!")
