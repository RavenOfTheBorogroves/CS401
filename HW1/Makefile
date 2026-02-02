
FILE = commerce
CXXFLAGS = -Wall -g

build: $(FILE).cpp
	g++ -Wall -g $(FILE).cpp -o $(FILE) -lm -fno-pie -no-pie

.PHONY: db

db:
	gdb -tui $(FILE)

run:
	./$(FILE)