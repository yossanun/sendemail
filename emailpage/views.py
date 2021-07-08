from django.shortcuts import render

def email(request):
    return render(request, 'emailpage/index.html')