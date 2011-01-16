#!/usr/bin/env python

from ctypes import *

from programme.selection.paper import Paper

constrain = CDLL('constraints_satisfaction/libconstrain.so')

def caller(ptr, size):
	print ptr, size
	for x in range(size):
		print 'ptr[%d]' % x, ptr[x],
	print 'finished calling'

    

CALLFUNC = CFUNCTYPE(None, POINTER(c_int), c_int)
SEARCHFUNC = CFUNCTYPE(None, c_int)

run = constrain.run
run.argtypes = [POINTER(c_int), c_int]
run.restype = None

papers = (c_int*2)(159101, 158100)

paper_search = Paper()

run(papers, len(papers), 
    CALLFUNC(caller), 
    SEARCHFUNC(paper_search))

