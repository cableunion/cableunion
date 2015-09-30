# -*- coding: utf-8 -*-
import random
import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

try:
    import cStringIO as StringIO
except:
    import StringIO

_letter_cases = "abcdefghijklmnopqrstuvwxyz"
_upper_case = _letter_cases.upper()
_numbers = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_cases, _upper_case, _numbers))


def create_validate_code(size=(120, 30),
                         chars=init_chars,
                         img_type="GIF",
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(0, 0, 255),
                         font_size=18,
                         font_type=os.path.join(os.path.dirname(__file__), 'captcha_font/times.ttf').replace('\\', '/'),
                         length=4,
                         draw_lines=True,
                         n_line=(1, 2),
                         draw_points=True,
                         point_chance=2):
    '''
        @todo: 生成验证码图片
        @param size: 图片的大小，格式（宽，高），默认为(120, 30)
        @param chars: 允许的字符集合，格式字符串
        @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
        @param mode: 图片模式，默认为RGB
        @param bg_color: 背景颜色，默认为白色
        @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
        @param font_size: 验证码字体大小
        @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
        @param length: 验证码字符个数
        @param draw_lines: 是否划干扰线
        @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
        @param draw_points: 是否画干扰点
        @param point_chance: 干扰点出现的概率，大小范围[0, 100]
        @return: [0]: PIL Image实例
        @return: [1]: 验证码图片中的字符串
    '''

    width, height = size #宽，高
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔
    print font_type

    def get_chars():
        '''生成给定长度的字符串，返回列表格式'''
        return random.sample(chars, length)

    def create_lines():
        '''绘制干扰线'''
        line_num = random.randint(*n_line) # 干扰线条数

        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            # 结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        '''绘制干扰点'''
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        '''绘制验证码字符'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars) # 每个字符前后以空格隔开
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3), strs, font=font, fill=fg_color)

        return ''.join(c_chars)

    if draw_lines:
        create_lines()

    if draw_points:
        create_points()

    strs = create_strs()

    params = [
        1 - float(random.randint(1, 2)) / 100,
        0,
        0,
        0,
        1 - float(random.randint(1, 10)) / 100,
        float(random.randint(1, 2)) / 500,
        0.001,
        float(random.randint(1, 2)) / 500
    ]

    img = img.transform(size, Image.PERSPECTIVE, params)

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, strs

# 每次生成验证码，都要先保存生成的图片，再显示到页面。这么做让人太不能接受了。
# 这个时候，我们需要使用python内置的StringIO模块，它有着类似file对象的行为，但是它操作的是内存文件。

@csrf_exempt
def get_captcha(request):
    currDir = sys.path[0]
    url_captchas = 'common/static/img/captchas/'
    # mstream = StringIO.StringIO()
    validate_code = create_validate_code()
    # 图片
    img = validate_code[0]
    # 先删除已经生成的图片
    removeFile(currDir + '/' + url_captchas, '.gif')
    img.save(url_captchas + 'captcha.gif', "GIF")
    # 文字
    request.session['validate'] = validate_code[1]
    response = HttpResponse()
    response['Pragma'] = "no-cache"
    response['Expires'] = "0"
    return response


# @csrf_exempt
# def validate(request):
#     mstream = StringIO.StringIO()
#     validate_code = create_validate_code()
#     img = validate_code[0]
#     img.save(mstream, "GIF")
#     request.session['validate'] = validate_code[1]
#     return HttpResponse(mstream.getvalue(), "image/gif")


def removeFile(dir, postfix):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            removeFile(dir + '/' + file, postfix)
    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)
