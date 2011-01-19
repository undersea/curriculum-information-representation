
SOURCES = degree.cpp propagator.cpp

OBJECTS=$(SOURCES:.cpp=.o)

CXXFLAGS = -Iinclude -fPIC -Wall -pedantic -ansi -std=c++0x `python-config --includes`
LDXXFLAGS = -Llib -lgecodeint -lgecodesearch -lgecodesupport -lgecodeminimodel -lgecodekernel -lgecodeset

LIBRARY_NAME = libconstrain.so

all:	$(OBJECTS) $(LIBRARY_NAME)


libconstrain.so:	$(OBJECTS)
	$(CXX) -shared -Wl,-soname,$(LIBRARY_NAME).1 -o $(LIBRARY_NAME) $(LDXXFLAGS) $(OBJECTS)


.cpp:
	$(CC) $(CXXFLAGS) $< -o $@

.phony: clean

clean:
	$(RM) $(OBJECTS)