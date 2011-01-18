#!/usr/bin/env python

from ctypes import *
from numpy import *

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

allocated_arrays = []
def valid_paper(degree, size):
        size[0] = 3
        pa = zeros((1, 3), dtype=c_int)
        pa[0,0] = 161101
        pa[0,1] = 160101
        pa[0,2] = 159101
        
        allocated_arrays.append(pa)
        ptr = pa.ctypes.data_as(c_void_p).value
        return ptr


CALLFUNC = CFUNCTYPE(None, c_int, POINTER(c_int), POINTER(c_int))
SEARCHFUNC = CFUNCTYPE(None, c_int)
VALIDFUNC = CFUNCTYPE(c_void_p, c_int, POINTER(c_int))

run = constrain.run
run.restype = None

papers = (c_int*2)(159101, 158100)
paper_search = Paper()

degrees = (c_int * 2)(5,10);

run(papers, len(papers),
    degrees, len(degrees), 
    CALLFUNC(caller),
    VALIDFUNC(valid_paper))
