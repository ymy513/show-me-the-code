#!/usr/bin/env python
import os, sys
import Image
import argparse



def resize(path,size):
    for infile in os.listdir(path):
        outfile = os.path.splitext(infile)[0]+".thumbnail"
        if infile!=outfile:
            im=Image.open(os.path.join(path,infile))
            im.thumbnail(size,Image.ANTIALIAS)
            im.save(os.path.join(path,outfile),"JPEG")
        
if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Resize images")
    parser.add_argument('-path',nargs='*')
    parser.add_argument('-size',nargs='*',type = int)
    args = parser.parse_args()
    print args.path[0], args.size
    resize(args.path[0],args.size)