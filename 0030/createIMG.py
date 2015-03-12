#!/usr/bin/env python
# coding=utf-8
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def  createIMG():
    mode = "RGB"
    bg_color = "white"
    fg_color = "black"
    length = 700
    wigth = 50
    size = (length,wigth)
    resize = (400,400)
    font_size = 50
    font_path = "/System/Library/Fonts/STHeiti Light.ttc"
    message1 = "喜欢你的人很多，不差我一个"
    message2 = "我喜欢的人很少，除了你就没了"
    alpha = 0.5

    img = Image.new(mode,size,bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path,font_size)
    draw.text((0,0),unicode(message1,"utf-8"),fg_color,font)

    img2 = Image.new(mode,size,bg_color)
    draw2 = ImageDraw.Draw(img2)
    font = ImageFont.truetype(font_path,font_size)
    draw2.text((0,0),unicode(message2,"utf-8"),fg_color,font)
    
    img = img.transform(resize, Image.QUAD, (0,0,0,wigth,length,wigth,length,0)) 
    img2 = img2.transform(resize, Image.QUAD, (0,0,0,wigth,length,wigth,length,0)) 
    img2 = img2.transpose(Image.ROTATE_90)
  
    img = Image.blend(img,img2,alpha)
    img.show()
    # img2.show()
    img.save(message1+'.jpg')

if __name__ == "__main__":
    createIMG()