from django.shortcuts import render

def index_en(request):
    return render(request, 'landing/index_en.html')

def index_ru(request):
    return render(request, 'landing/index_ru.html')
