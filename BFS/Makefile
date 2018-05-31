.PHONY: default
default: all ;
CC=g++
CFLAGS=-ll
ODIR=.
INCDIR=.
TESTDIR=.
BINDIR=.
BIN=bfs


bfs.o:
	$(CC) bfs.cpp -o $(BIN)

all: bfs.o
	$(BINDIR)/bfs 
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(BIN)
