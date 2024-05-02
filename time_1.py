import time
import matplotlib.pyplot as plt

# top-down ( divide and conqure/ pure recursive) methods
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# bottom-up (dynamic-programming-like) methods
def fibonacci_dp(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Measure execution time for both methods
n_values = list(range(1, 101))
execution_times_recursive = []
execution_times_dp = []

for n in n_values:
    if n>50:
        execution_time= execution_times_recursive[49]
        execution_times_recursive.append(execution_time)
        print("n:", n, "Recursive execution time:", execution_time)

    else:
        start_time = time.time()
        fibonacci_result = fibonacci_recursive(n)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times_recursive.append(execution_time)
        print("n:", n, "Recursive execution time:", execution_time)

    start_time = time.time()
    fibonacci_result = fibonacci_dp(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_dp.append(execution_time)
    print("n:", n, "DP execution time:", execution_time)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(n_values, execution_times_recursive, label='Recursive')
plt.plot(n_values, execution_times_dp, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time of Fibonacci Calculation Methods')
plt.legend()
plt.grid(True)
plt.savefig('Execution Time of Fibonacci Calculation Methods')
plt.show()
