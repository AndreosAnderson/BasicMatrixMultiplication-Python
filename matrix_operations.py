# matrix_operations.py
import numpy as np
import psutil
import time
from memory_profiler import memory_usage

def matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def track_memory(func, *args):
    mem_usage = memory_usage((func, args))
    print(f"Memory usage: {max(mem_usage)} MB")
    return mem_usage

def track_cpu(func, *args):
    cpu_percent_before = psutil.cpu_percent(interval=1)
    start_time = time.time()

    func(*args)

    end_time = time.time()
    cpu_percent_after = psutil.cpu_percent(interval=1)

    print(f"Initial CPU usage: {cpu_percent_before}%")
    print(f"Final CPU usage: {cpu_percent_after}%")
    print(f"Execution time: {end_time - start_time} seconds")
