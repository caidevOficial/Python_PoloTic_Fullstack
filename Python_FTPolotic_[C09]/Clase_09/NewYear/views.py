from django.shortcuts import render
import datetime

# Create your views here.

def answer(request):
    now = datetime.datetime.now()
    return render(request, "NewYear/answer.html",{"NewYear": now.month == 1 and now.day == 1})

def index(request):
    return render(request, "NewYear/index.html")