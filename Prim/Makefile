.PHONY: default
default: all ;
CC=g++
CFLAGS=-ll
ODIR=.
INCDIR=.
TESTDIR=.
BINDIR=.
BIN=prim


prim.o:
	$(CC) prim.cpp -o $(BIN)

exe: prim.o
	$(BINDIR)/prim > output.dot

all: exe
	dot -Tps output.dot -o prim_output.ps
	
clean:
	rm -f $(ODIR)/*.o $(ODIR)/*.dot $(ODIR)/*.ps *~ core $(INCDIR)/*~ $(BIN)
