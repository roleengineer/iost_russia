from django.shortcuts import render

def dev_en(request):
    return render(request, 'dev/dev_en.html')

def dev_ru(request):
    return render(request, 'dev/dev_ru.html')
