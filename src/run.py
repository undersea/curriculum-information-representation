#!/usr/bin/env python

from ctypes import *

from programme.selection.paper import Paper

constrain = CDLL('constraints_satisfaction/libconstrain.so')

def caller(degree, ptr, size):
	print degree, ptr, size
        try:
                for x in range(size):
                        print 'ptr[%d]' % x, ptr[x],
        except Exception, e:
                print "A error occured: %s" % (str(e))
	print 'finished calling'

def valid_paper(degree, size):
        size[0] = 2
        pa = (c_int*2)()
        pa[0] = 161101
        pa[1] = 160101
        return pointer(pa)

size = POINTER(c_int)(c_int(-1))
print type(valid_paper(0, size))
print size[0]

def test(pointer):
        resize(pointer, 64)
        pointer[0] = 1
        pointer[1] = 2

pointer = POINTER(c_int)(c_int(-1))
test(pointer)
print pointer[0], pointer[1]
        
CALLFUNC = CFUNCTYPE(None, c_int, POINTER(c_int), POINTER(c_int))
SEARCHFUNC = CFUNCTYPE(None, c_int)
VALIDFUNC = CFUNCTYPE(POINTER(c_int), c_int, POINTER(c_int))

run = constrain.run
run.restype = None

papers = (c_int*2)(159101, 158100)
paper_search = Paper()

degrees = (c_int * 2)(5,10);

run(papers, len(papers),
    degrees, len(degrees), 
    CALLFUNC(caller),
    VALIDFUNC(valid_paper))

