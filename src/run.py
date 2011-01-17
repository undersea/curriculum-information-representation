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

def valid_paper(degree, paper):
        print 'is valid %d, %d' % (degree, paper)
        return True

CALLFUNC = CFUNCTYPE(None, c_int, POINTER(c_int), c_int)
SEARCHFUNC = CFUNCTYPE(None, c_int)
VALIDFUNC = CFUNCTYPE(c_int, c_int, c_int)

run = constrain.run
run.restype = None

papers = (c_int*2)(159101, 158100)
paper_search = Paper()


run(papers, len(papers), 
    CALLFUNC(caller), 
    SEARCHFUNC(paper_search),
    VALIDFUNC(valid_paper))

