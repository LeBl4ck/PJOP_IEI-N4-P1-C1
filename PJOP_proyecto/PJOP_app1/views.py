from django.shortcuts import render
from django.http import HttpResponse
def vista1(request):
    html="""
    <h3 style="background-color: yellow"> ESTA ES APP1 VISTA 1</h3>
    """
    return HttpResponse(html)

def vista2(request):
    html="""
    <h4 style="background-color: orange"> ESTA ES APP1 VISTA 2</h4>
    """
    return HttpResponse(html)