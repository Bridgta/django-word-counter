from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello')


def dogs(request):
    return HttpResponse('Dogs are great!')