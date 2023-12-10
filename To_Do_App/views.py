from django.shortcuts import render


def home(request):
    return render(request, 'To_Do_App/indx.html')
