import time
import random
import numpy as np
from scipy.stats import chisquare
import LCG
import MCG


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    deviations = [(x - mean) ** 2 for x in numbers]
    variance = sum(deviations) / len(numbers)
    return variance ** 0.5


def calculate_coefficient_of_variation(numbers):
    mean = calculate_mean(numbers)
    std_dev = calculate_standard_deviation(numbers)
    return (std_dev / mean) * 100


def calculate_chi_square(numbers, num_intervals):
    observed_frequencies, _ = np.histogram(numbers, bins=num_intervals)
    expected_frequencies = [len(numbers) / num_intervals] * num_intervals
    chi2, p = chisquare(observed_frequencies, f_exp=expected_frequencies)
    return chi2, p


def chi_square_test(samples, num_intervals):
    chi_square_results = []
    for sample in samples:
        chi_square_results.append(calculate_chi_square(sample, num_intervals))
    return chi_square_results


def print_chi_square_results(chi_square_results, num_intervals):
    pass_count = 0
    for i, result in enumerate(chi_square_results):
        chi2, p_value = result
        alpha = 0.05
        print("Sample", i + 1)
        print("Chi-square:", chi2)
        print("p-value:", p_value)
        if p_value >= alpha:
            pass_count += 1
            print("Uniform: True")
        else:
            print("Uniform: False")
        print("-------------------------")
    print("Pass count:", pass_count, "out of", len(chi_square_results))





num_samples = 10
sample_size = 50
num_intervals = 10

samples_lcg = []
samples_mcg = []
samples_random = []

lcg = LCG.LinearCongruentialGenerator(int(time.time()))
mcg = MCG.MultiplicativeCongruentialGenerator(int(time.time()))

for _ in range(num_samples):
   random_sample = [random.randint(0, 10000) for _ in range(sample_size)]
   lcg_sample = lcg.generate(sample_size)
   mcg_sample = mcg.generate(sample_size)

   samples_random.append(random_sample)
   samples_lcg.append(lcg_sample)
   samples_mcg.append(mcg_sample)

print("---- RANDOM ----- \n \n")
for i, sample in enumerate(samples_random):
    print("Sample", i + 1)
    print("Mean:", calculate_mean(sample))
    print("Standard Deviation:", calculate_standard_deviation(sample))
    print("Coefficient of Variation:", calculate_coefficient_of_variation(sample))
    print("-------------------------")

print("\n\n---- LINEAR ----- \n")
for i, sample in enumerate(samples_lcg):
    print("Sample", i + 1)
    print("Mean:", calculate_mean(sample))
    print("Standard Deviation:", calculate_standard_deviation(sample))
    print("Coefficient of Variation:", calculate_coefficient_of_variation(sample))
    print("-------------------------")

print("\n\n---- MULTIPLICATIVE ----- \n")
for i, sample in enumerate(samples_mcg):
    print("Sample", i + 1)
    print("Mean:", calculate_mean(sample))
    print("Standard Deviation:", calculate_standard_deviation(sample))
    print("Coefficient of Variation:", calculate_coefficient_of_variation(sample))
    print("-------------------------")

chi_square_results_rand = chi_square_test(samples_random, num_intervals)
print(" \n\n---- Random Python Generator ---- ")
print_chi_square_results(chi_square_results_rand, num_intervals)


chi_square_results_lcg = chi_square_test(samples_lcg, num_intervals)
print(" \n\n---- Linear Congruential Generator ---- ")
print_chi_square_results(chi_square_results_lcg, num_intervals)

chi_square_results_mcg = chi_square_test(samples_mcg, num_intervals)
print(" \n\n---- Multiplicative Congruential Generator ---- ")
print_chi_square_results(chi_square_results_mcg, num_intervals)



