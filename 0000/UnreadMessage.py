#!/usr/bin/env python
import Image
import ImageDraw
import ImageFont

class UnreadMessage(object):
	def __init__(self):
		self.fnt = None
		self.im = None

	def open(self, path):
		self.im = Image.open(path)

	def setFont(self, font_path, size):
		self.fnt = ImageFont.truetype(font_path, size)  

	def draw_text(self, position, message, colour, fnt):
		drawSurface = ImageDraw.Draw(self.im)
		drawSurface.text(position, message, fill=colour, font=fnt)
		self.im.show()
		self.im.save('draw'+message+'.jpg')

test = UnreadMessage()
test.open("test.jpg")
test.setFont("/System/Library/Fonts/Helvetica.dfont",80)
test.draw_text((180,20),'4',(255,0,0),test.fnt)
