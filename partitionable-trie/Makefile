.PHONY: default
default: all ;
CC=gcc
LEX=flex
YACC=bison
CFLAGS=
ODIR=.
INCDIR=.
TESTDIR=.
BINDIR=.
BIN=partitionable

partitionable.o:
	$(CC) partitionable.c -o $(BIN) $(CFLAGS)

all: partitionable.o
	$(BINDIR)/$(BIN) 
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ types_size $(BIN)
