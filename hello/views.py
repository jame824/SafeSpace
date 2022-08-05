from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def getinvolved(request):
    return render(request, 'getinvolved.html')

def resources(request):
    return render(request, 'resources.html')

def community(request):
    return render(request, 'community.html')