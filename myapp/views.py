from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def practice(request):
    print(isinstance(request, HttpRequest))
    print(request.user)
    # return HttpResponse("<p>Here's the text of the Web page.</p>")

    context = {
        "name": "Bob",
        "age": 99
    }
    return render(request, 'myapp/main.html', context)
    