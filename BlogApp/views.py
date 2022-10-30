from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
import json
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def login(request):
    if request.method == "POST":
        data = request.data
        return JsonResponse(data)
    return render(request, "login.html") 


# 获取图片验证码
def get_random_code(request):
    fp = open("./BlogApp/utils/code/code.png", "rb")

    data = fp.read()
    fp.close()
    return HttpResponse(data)

def sign(request):
    return render(request, "sign.html")
