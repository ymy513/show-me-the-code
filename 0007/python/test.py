#!/usr/bin/env python
import gc,os,psutil

def test():
    x=0
    for i in range(10000):
        x+=i

    return x

def main():
    print test()
    gc.collect()
    p=psutil.Process(os.getpid())
    print p.get_memory_info()

if __name__=="__main__":
    main()
