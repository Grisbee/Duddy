from django.shortcuts import render
# Create your views here.



def homepage(request):
    return render(request, "home/homepage.html")


def test(request):
    return render(request, "home/base.html")


def map_page(request):
    return render(request, "home/map.html")

