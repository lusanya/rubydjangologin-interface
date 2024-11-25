

from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request,'signup.html')
def reset(request):
    return render(request, 'resetpassword.html')
