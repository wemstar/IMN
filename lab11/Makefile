all: compile link clean run 
	
link:
	g++ -o Macura_11 *.o
compile:
	g++ -c *.cpp
run:
	./Macura_11
	gnuplot Macura_11.gpl
clean:
	rm *.o
