MAINPROG=precisionEstimate

SOURCES:=$(wildcard *.cpp)
OBJECTS=$(SOURCES:.cpp=.o)
FLAGS=-std=c++17 -fsanitize=address -fuse-ld=gold -Wall -MMD \
      -fext-numeric-literals -lquadmath #-O3

all: $(SOURCES) $(MAINPROG)

$(MAINPROG): $(OBJECTS)
	g++ $(FLAGS) $(OBJECTS) -o $@

.cpp.o:
	g++ $(FLAGS) -c $< -o $@

clean:
	rm *.o $(MAINPROG)
