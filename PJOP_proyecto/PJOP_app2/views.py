from django.shortcuts import render
from django.http import HttpResponse
def vista1(request):
    html="""
    <div style="background-color: green"> ESTA ES APP1 VISTA 1</div>
    """
    return HttpResponse(html)

def vista2(request):
    html="""
    <h1 style="background-color: green"> ESTA ES APP1 VISTA 1</h1>
    """
    return HttpResponse(html)

