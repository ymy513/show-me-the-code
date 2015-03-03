import os, sys
import Image

size=1136,640

for infile in os.listdir(sys.argv[1]):
    outfile = os.path.splitext(infile)[0]+".thumbnail"
    if infile!=outfile:
        try:
            im=Image.open(sys.argv[1]+"/"+infile)
            im.thumbnail(size,Image.ANTIALIAS)
            im.save(sys.argv[1]+"/"+outfile,"JPEG")
        except IOError:
            print "cannot create thumnail for '%s'" % infile