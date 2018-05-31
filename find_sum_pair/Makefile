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
BIN=find_sum_pair

find_sum_pair.o:
	$(CC) find_sum_pair.cpp -o $(BIN) $(CFLAGS)

all: find_sum_pair.o
	$(BINDIR)/$(BIN)
	
clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ types_size $(BIN)
