from urllib import response
from django.utils.deprecation import MiddlewareMixin
from requests import request
import json

# 解析post请求数据
class POST_DECODE_MD(MiddlewareMixin):
    # 请求中间件
    def process_request(slef, request):
        if request.method == "POST":
            data = json.loads(request.body)  # request.body 请求体 存放json数据
            # data = json.loads(request.body, encoding="utf-8")
            request.data = data

    def process_response(self, request, response):
        return response