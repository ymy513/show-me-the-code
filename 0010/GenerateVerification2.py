#!/usr/bin/env python
#coding=utf-8
 
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

 
_letter_cases = "abcdefghijklmnopqrstuvwxyz" 
_upper_cases = _letter_cases.upper() 
_numbers = ''.join(map(str, range(3, 10))) 
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
 
def create_validate_code(size=(120, 30),
                         chars=init_chars,
                         img_type="GIF",
                         mode="RGB",
                         bg_color="white",
                         fg_color="red",
                         font_size=18,
                         font_type="/System/Library/Fonts/Helvetica.dfont",
                         length=4,
                         point_chance = 2):
   
 
    width, height = size 
    img = Image.new(mode, size, bg_color) 
    draw = ImageDraw.Draw(img) 
 
    def get_letters():
        return random.sample(chars, length)
 
    def create_lines():
        line_num = random.randint(1,4) # 干扰线条数
        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))
 
    def create_points():
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]     
        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))
 
    def create_strs():
        letters = get_letters()
        strs = ' %s ' % ' '.join(letters) 
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 2, (height - font_height) / 2),
                    strs, fill=fg_color, font=font)       
        return ''.join(letters)
 
    create_lines()
    create_points()
    strs = create_strs()
 
    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲 
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大） 
    return img
 
if __name__ == "__main__":
    im = create_validate_code()
    im.save("VerificationCode.png")