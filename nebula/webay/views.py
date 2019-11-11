from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webay/index.html')


def profile(request):
    return render(request, 'webay/profile.html')
