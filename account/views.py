from django.http import HttpResponse
import datetime


def helloworld(request):
    return HttpResponse("hello world")


def mydatetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)