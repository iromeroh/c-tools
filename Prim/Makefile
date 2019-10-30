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
	$(BINDIR)/prim prim > output1.dot

orig: exe
	$(BINDIR)/prim show > output2.dot

gr1: orig
	dot -Tpdf output1.dot -o prim_output.pdf

all: gr1
	dot -Tpdf output2.dot -o original_graph.pdf
	
clean:
	rm -f $(ODIR)/*.o $(ODIR)/*.dot $(ODIR)/*.pdf *~ core $(INCDIR)/*~ $(ODIR)/$(BIN)
