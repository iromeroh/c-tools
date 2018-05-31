.PHONY: default
default: all ;
CC=g++
LEX=flex
YACC=bison
CFLAGS=-std=c++11
ODIR=.
INCDIR=.
TESTDIR=.
BINDIR=.
BIN=zero_sum

zero_sum.o:
	$(CC) zero_sum.cpp -o $(BIN) $(CFLAGS)

all: zero_sum.o
	$(BINDIR)/zero_sum 
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ types_size $(BIN)
