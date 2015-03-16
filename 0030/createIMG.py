#!/usr/bin/env python
# coding=utf-8
import random
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def  createIMG(m,size,output_size,output_file,is_show):
    mode = "RGB"
    bg_color = "white"
    fg_color = "black"
    length = size[0]
    width = size[1]
    size = (length,width)
    resize = (output_size[0],output_size[0])
    font_size = 50
    font_path = "/System/Library/Fonts/STHeiti Light.ttc"
    #message1 = "喜欢你的人很多，不差我一个"
    #message2 = "我喜欢的人很少，除了你就没了"
    message1 = m[0]
    message2 = m[1] 
    alpha = 0.5

    img = Image.new(mode,size,bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path,font_size)
    draw.text((0,0),unicode(message1,"utf-8"),fg_color,font)

    img2 = Image.new(mode,size,bg_color)
    draw2 = ImageDraw.Draw(img2)
    font = ImageFont.truetype(font_path,font_size)
    draw2.text((0,0),unicode(message2,"utf-8"),fg_color,font)
    
    img = img.transform(resize, Image.QUAD, (0,0,0,width,length,width,length,0)) 
    img2 = img2.transform(resize, Image.QUAD, (0,0,0,width,length,width,length,0)) 
    img2 = img2.transpose(Image.ROTATE_90)
  
    img = Image.blend(img,img2,alpha)
    if(is_show):
        img.show()
    # img2.show()
    img.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create image of love")
    # -m "喜欢你的人很多，不差我一个" "我喜欢的人很少，除了你就没了" -size 700,50 --output_size 400 -o out.jpg [--show]
    parser.add_argument('-m',nargs = '*')
    parser.add_argument('-size',nargs = '*',type = int)
    parser.add_argument('--output_size',nargs = 1,type = int)
    parser.add_argument('-o',nargs = '?')
    parser.add_argument('--show',action='store_true')
    args = parser.parse_args()
    #print args
    createIMG(args.m, args.size, args.output_size, args.o, args.show)