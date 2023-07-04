# Copyright 2017 Meritxell Jordana Gavieiro
# Copyright 2017 Albert Merino Pulido
# Copyright 2017 Marc Sánchez Fauste

SERIAL_TARGET_BB=knapsackBB_serial
MPI_TARGET_BB=knapsackBB_mpi
SERIAL_TARGET_DYN=knapsackDYN_serial
MPI_TARGET_DYN=knapsackDYN_mpi
RESULTS=results.csv
RESULTS_SPEEDUPS=results_speedups.csv
RESULTS_TIMES=results_times_per_problem.csv
RESULTS_SPEEDUPS_PER_PROBLEM=results_speedups_per_problem.csv
PLOT_FILENAME=results_times_per_problem.svg
PLOT_SPEEDUPS_FILENAME=results_speedups_per_problem.svg
OUTPUT_FOLER=output
ERROR_FOLDER=errors
THREADS_FILE=threads.csv

all : serial mpi

dyn : $(SERIAL_TARGET_DYN) $(MPI_TARGET_DYN)

serial : $(SERIAL_TARGET_DYN)

$(SERIAL_TARGET_DYN) : knapsackDYN_serial.c
	gcc-12 knapsackDYN_serial.c -o $(SERIAL_TARGET_DYN)

mpi : $(MPI_TARGET_DYN)

$(MPI_TARGET_DYN) : knapsackDYN_mpi.c
	mpicc knapsackDYN_mpi.c -o $(MPI_TARGET_DYN)

# run-local : d
# 	./run_all_local.sh

# run-moore : bb
# 	./run_all.sh

# results : $(RESULTS) $(RESULTS_TIMES) $(RESULTS_SPEEDUPS) $(RESULTS_SPEEDUPS_PER_PROBLEM)

# $(RESULTS) : $(OUTPUT_FOLER)/*
# 	./get_results.sh > $(RESULTS)

# $(RESULTS_TIMES) : $(RESULTS) $(THREADS_FILE)
# 	python3.10 get_times_per_problem.py $(RESULTS) $(THREADS_FILE) > $(RESULTS_TIMES)

# $(RESULTS_SPEEDUPS) : $(RESULTS)
# 	python3.10 get_speedups.py $(RESULTS) > $(RESULTS_SPEEDUPS)

# $(PLOT_FILENAME) : $(RESULTS_TIMES) $(THREADS_FILE)
# 	python3.10 plot_generator.py $(RESULTS_TIMES) $(THREADS_FILE) $(PLOT_FILENAME)

# $(PLOT_SPEEDUPS_FILENAME) : $(RESULTS_SPEEDUPS_PER_PROBLEM) $(THREADS_FILE)
# 	python3.10 plot_speedups_generator.py $(RESULTS_SPEEDUPS_PER_PROBLEM) \
# 		$(THREADS_FILE) $(PLOT_SPEEDUPS_FILENAME)

# $(RESULTS_SPEEDUPS_PER_PROBLEM) : $(RESULTS_SPEEDUPS) $(THREADS_FILE)
# 	python3.10 get_speedups_per_problem.py $(RESULTS_SPEEDUPS) $(THREADS_FILE) \
# 		> $(RESULTS_SPEEDUPS_PER_PROBLEM)

# plot : $(PLOT_FILENAME) $(PLOT_SPEEDUPS_FILENAME)

clean : clean-outputs clean-errors
	rm -rf $(MPI_TARGET_DYN) $(SERIAL_TARGET_DYN) $(RESULTS) $(PLOT_FILENAME) \
		$(RESULTS_SPEEDUPS) $(RESULTS_TIMES) $(THREADS_FILE) \
		$(PLOT_SPEEDUPS_FILENAME) $(PLOT_SPEEDUPS_FILENAME)

clean-outputs :
	rm -rf $(OUTPUT_FOLER)

clean-errors :
	rm -rf $(ERROR_FOLDER)
