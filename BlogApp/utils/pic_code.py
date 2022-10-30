from PIL import Image, ImageDraw, ImageFont
import string
import random

from pip import main

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

str_all = string.digits + string.ascii_letters
def random_code():
    width = 200
    height = 40

    # 生成尺寸为200*40的白色背景图片
    img = Image.new("RGB", (width, height), color=(255, 255, 255))

    # 创建一个和图片大小相同的画布
    draw = ImageDraw.Draw(img)

    # 生成字体对象
    font = ImageFont.truetype(
        font="MyBlog/BlogApp/utils/font/212_Saint_Paddy.ttf", size=32)

    # 书写文字
    volid_code = ""

    for i in range(4):
        random_char = random.choice(str_all)
        draw.text((40*i+20, 5), random_char, (0, 0, 0), font=font)
        volid_code += random_char
    print(volid_code)

    # 验证码图片混淆 
    for i in range(80):
        # 点混淆
        x,y = random.randint(0,width), random.randint(0,height)
        draw.point((x, y), random_color())

    # 随机画线
    for i in range(10):
        x1,y1 = random.randint(0,width), random.randint(0,height)
        x2,y2 = random.randint(0,width), random.randint(0,height)
        draw.line((x1,y1,x2,y2), random_color())

    img.save(r'MyBlog/BlogApp/utils/code_pic/code.png', "PNG")

if __name__ == "__main__":
    random_code()