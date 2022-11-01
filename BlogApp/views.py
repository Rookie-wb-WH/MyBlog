from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
import json
import os

from idna import valid_contextj
from BlogApp.utils.random_code import random_code

# Create your views here.

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def login(request):
    if request.method == "POST":
        res = {
            "code": 425,
            "msg": "登录成功!",
            "self": None
        }
        data = request.data
        username = data.get("username")
        password = data.get("password")
        code = data.get("code")


        valid_code: str = request.session.get("valid_code")
        if valid_code.upper() == data.get("code").upper():
            res["code"] = 0
        else:
            res["msg"] = "验证码输入错误!"
            res["self"] = res["code"]
        return JsonResponse(res)
    return render(request, "login.html") 


# 获取图片验证码
def get_random_code(request):
    data, valid_code = random_code()
    request.session['valid_code'] = valid_code
    return HttpResponse(data)

def sign(request):
    return render(request, "sign.html")
