#!/usr/bin/env python
import os, sys
import Image

size=1136,640

for infile in os.listdir(sys.argv[1]):
    outfile = os.path.splitext(infile)[0]+".thumbnail"
    if infile!=outfile:
        im=Image.open(os.path.join(sys.argv[1],infile))
        im.thumbnail(size,Image.ANTIALIAS)
        im.save(os.path.join(sys.argv[1],outfile),"JPEG")
        