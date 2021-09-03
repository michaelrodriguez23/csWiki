from django.shortcuts import render

def entry(request, title):
    return render(request, "wiki/title.html", {
        title : title.capitalize
    })

