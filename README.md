# Implementation-of-Knapsack-0-1-problem-in-MPI-OpenMP
STEPS:

OpenMP:
0. Run generator.py arg1(knapsack) arg2(weight) create the data you want.
1. Copy the files under ‘problem_sets’ folder to ‘testbed’ folder
2. Run make
3. Run ./run_all_local.sh
4. Make results
5. Make plot

MPI:
1. Use the files you just generate in OpenMP
2. Run make
3. Run mpirun -np <yours process> mpi <yours data>
4. Record results and use the tools in OpenMP folder to plot

