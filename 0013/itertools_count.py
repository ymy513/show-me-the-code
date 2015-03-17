# https://docs.python.org/2/library/itertools.html#itertools.count
# encoding=utf-8
class itertoos(object):
    # count(10)-->10,11,12,13,……
    # count(2.5,0.5)-->2.5,3,3.5,4,……
    def count(self,start,step):    
        n = start
        while True:
            yield n
            n +=step

    # start + step * i for i in count()