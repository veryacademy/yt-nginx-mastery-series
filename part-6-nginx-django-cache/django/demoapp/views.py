from django.shortcuts import render
from django.views.decorators.cache import cache_control

@cache_control(private=True)
def homepage(request):
    return render(request, "p1.html")