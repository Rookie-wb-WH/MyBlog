import re
from django import template

# 注册
register = template.Library()

@register.inclusion_tag('MyTag/headers.html')
def banner(MenuName):
    ImgList = [
        "../static/my/BannerImg/1.jpg",
        "../static/my/BannerImg/2.jpg",
        "../static/my/BannerImg/3.jpg",
        "../static/my/BannerImg/4.jpg",
        "../static/my/BannerImg/5.jpg",
        "../static/my/BannerImg/6.jpg",
        "../static/my/BannerImg/7.jpg",
        "../static/my/BannerImg/8.jpg",
        "../static/my/BannerImg/9.jpg",
        "../static/my/BannerImg/10.jpg"
    ]
    return {"ImgList": ImgList}
