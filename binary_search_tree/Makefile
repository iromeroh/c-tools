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
BIN=bst

bst.o:
	$(CC) bst.c -o $(BIN) $(CFLAGS)

all: bst.o
	$(BINDIR)/$(BIN)
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(BIN)
