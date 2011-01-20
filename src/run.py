#!/usr/bin/env python

from ctypes import *
from numpy import *

from programme.selection.paper import Paper

constrain = CDLL('constraints_satisfaction/libconstrain.so')

def caller(degree, ptr, size):
	print degree, ptr[0], size
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



def in_degree(size):
    print 'python in_degree'
    degrees = zeros((1, 5), dtype=c_int)
    degrees[0,0] = 1
    degrees[0,1] = 2
    degrees[0,2] = 3
    degrees[0,3] = 4
    degrees[0,4] = 5
    allocated_arrays.append(degrees)
    ptr = degrees.ctypes.data_as(c_void_p).value
    size[0] = 5
    return ptr


INDEGREE = CFUNCTYPE(c_void_p, POINTER(c_int))
CALLFUNC = CFUNCTYPE(None, c_int, POINTER(c_int), c_int)
SEARCHFUNC = CFUNCTYPE(None, c_int)
VALIDFUNC = CFUNCTYPE(c_void_p, c_int, POINTER(c_int))

setter = INDEGREE(in_degree)

#set_degrees = constrain.set_degrees_function
#set_degrees.restype = None
#set_degrees(setter)

#constrain.init()

run = constrain.run
run.restype = None

papers = (c_int*6)(159101, 159101, 158100, 160101, 161101, 160102)
paper_search = Paper()

degrees = (c_int * 25)(159101, 159102, 159201, 159202, 159233, 159234, 159235, 159253, 159254, 158359, 159302, 159331, 159333, 159334, 159335, 159339, 159351, 159354, 159355, 159356, 159357, 159359, 161326  )

print len(degrees)

run(papers, len(papers),
    degrees, len(degrees), 
    CALLFUNC(caller))#,
    #VALIDFUNC(valid_paper))
