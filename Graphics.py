import time
import random
import matplotlib.pyplot as plt
import LCG
import MCG

def plot_time_comparison():
    sample_sizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000]
    times_lcg = []
    times_mcg = []
    times_random = []

    for size in sample_sizes:
        lcg = LCG.LinearCongruentialGenerator(int(time.time()))
        mcg = MCG.MultiplicativeCongruentialGenerator(int(time.time()))
        random_start_time = time.time()
        random_sample = [random.randint(0, size) for _ in range(size)]
        random_end_time = time.time()

        lcg_start_time = time.time()
        lcg_sample = lcg.generate(size)
        lcg_end_time = time.time()

        mcg_start_time = time.time()
        mcg_sample = mcg.generate(size)
        mcg_end_time = time.time()

        times_random.append(random_end_time - random_start_time)
        times_lcg.append(lcg_end_time - lcg_start_time)
        times_mcg.append(mcg_end_time - mcg_start_time)

    plt.plot(sample_sizes, times_random, label="random", color ='#5E8CB8', linewidth = 1.5, marker ='*')
    plt.plot(sample_sizes, times_lcg, label="linear congruential generator", color ='#CE81AD', linewidth = 1.5, marker = '+')
    plt.plot(sample_sizes, times_mcg, label="multiplicative congruential generator", color ='#76BFBF', linewidth = 1.5, marker = 'o')
    plt.xlabel("Sample Size")
    plt.ylabel("Time (seconds)")
    plt.title("Time Comparison")
    plt.legend()
    plt.show()

plot_time_comparison()
