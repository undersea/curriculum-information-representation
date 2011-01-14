from ctypes import *

constrain = CDLL('./libconstrain.so')

def caller(ptr, size):
	for x in range(size):
		print 'caller', ptr[x],
	print

CMPFUNC = CFUNCTYPE(None, POINTER(c_int), c_int)

run = constrain.run
run.argtypes = [POINTER(c_int), c_int]
run.restype = None

papers = (c_int*2)(159101, 158100)

run(papers, len(papers), CMPFUNC(caller))

