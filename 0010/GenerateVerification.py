#!/usr/bin/env python

import random
import string
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
 
def get_letters():
    letters = ''
    for n in xrange(4):
        letters += random.choice(string.ascii_letters)
    return letters.decode('utf-8')

def draw(letters):
    im = Image.new('1',(200,150),'white')
    draw = ImageDraw.Draw(im)
    draw.text((90,75),letters)
    im.save("VerificationCode.png")

def main():
    letters = get_letters()
    draw(letters)

if __name__=='__main__':
    main()