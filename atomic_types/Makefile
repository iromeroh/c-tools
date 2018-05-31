.PHONY: default
default: all ;
CC=gcc
LEX=flex
YACC=bison
CFLAGS=-ll
ODIR=.
INCDIR=.
TESTDIR=.
BINDIR=.


sizes.o:
	$(CC) atomic_types_sizes.c -o types_size

all: sizes.o
	$(BINDIR)/types_size 
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ types_size
