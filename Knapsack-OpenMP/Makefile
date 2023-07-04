CC = gcc-12
CGG = g++-12
SERIAL_TARGET_DYN=knapsackDYN_serial
SERIAL_TARGET_BB=knapsackBB_serial
OMP_TARGET_DYN=knapsackDYN_omp
OMP_TARGET_BB=knapsackBB_omp
RESULTS=results.csv
RESULTS_SPEEDUPS=results_speedups.csv
RESULTS_TIMES=results_times_per_problem.csv
OUTPUT_FOLER=output
ERROR_FOLDER=errors
PLOT_SPEEDUPS_FILENAME=results_speedups_per_problem.svg
THREADS_FILE=threads.csv
RESULTS_SPEEDUPS_PER_PROBLEM=results_speedups_per_problem.csv
PLOT_FILENAME=results_times_per_problem.svg


all : serial omp

dyn : $(SERIAL_TARGET_DYN) $(OMP_TARGET_DYN)

serial : $(SERIAL_TARGET_DYN) 

$(SERIAL_TARGET_DYN) : knapsackDYN_serial.c
# gcc-12 knapsackDYN_serial_optimized.c -o $(SERIAL_TARGET_DYN)
	$(CC) knapsackDYN_serial.c -o $(SERIAL_TARGET_DYN)

omp : $(OMP_TARGET_DYN) 

$(OMP_TARGET_DYN) : knapsackDYN_omp.c
	$(CC) -fopenmp knapsackDYN_omp.c -o $(OMP_TARGET_DYN)

run-local : dyn
	./run_all_local.sh

run-moore : dyn
	./run_all.sh

results : $(RESULTS) $(RESULTS_TIMES) $(RESULTS_SPEEDUPS) $(PLOT_SPEEDUPS_FILENAME) $(RESULTS_SPEEDUPS_PER_PROBLEM)

$(RESULTS) : $(OUTPUT_FOLER)/*
	./get_results.sh > $(RESULTS)

$(RESULTS_TIMES) : $(RESULTS)
	python3.10 get_times_per_problem.py $(RESULTS) > $(RESULTS_TIMES)

$(RESULTS_SPEEDUPS) : $(RESULTS)
	python3.10 get_speedups.py $(RESULTS) > $(RESULTS_SPEEDUPS)

$(PLOT_SPEEDUPS_FILENAME) : $(RESULTS_SPEEDUPS_PER_PROBLEM) $(THREADS_FILE)
	python3.10 plot_speedups_generator.py $(RESULTS_SPEEDUPS_PER_PROBLEM) \
		$(THREADS_FILE) $(PLOT_SPEEDUPS_FILENAME)

$(RESULTS_SPEEDUPS_PER_PROBLEM) : $(RESULTS_SPEEDUPS) $(THREADS_FILE)
	python3.10 get_speedups_per_problem.py $(RESULTS_SPEEDUPS) $(THREADS_FILE) \
		> $(RESULTS_SPEEDUPS_PER_PROBLEM)

plot : $(RESULTS_TIMES)
	python3.10 plot_generator.py $(RESULTS_TIMES)
# plot : $(PLOT_FILENAME) $(PLOT_SPEEDUPS_FILENAME)

clean :
	rm -rf $(SERIAL_TARGET_DYN) $(OMP_TARGET_DYN) $(RESULTS) $(RESULTS_SPEEDUPS) $(RESULTS_TIMES)

clean-outputs :
	rm -rf $(OUTPUT_FOLER)

clean-errors :
	rm -rf $(ERROR_FOLDER)

