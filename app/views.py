from django.shortcuts import render
from . import consumers

# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request,'index.html')

