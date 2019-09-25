# Author: Matt Trapani
# Date: 9/24/19
# Description:
''''
This program will generate random samples of size n from the exponential distribution with mean mu. The computer will
run 1,000 such samples. In each sample, the computer will calculate the sample mean. Next, it'll average the 1,000
sample means and find the variance of the 1,000 sample means. Finally, the program will display the observed sample mean
and variance against the theoretical sample mean and variances. A relative frequency histogram will be displayed to show
the shape of the data.
'''

from random import expovariate
from statistics import mean, variance
import matplotlib.pyplot as plt
import numpy as np

sample_size = 0
num_samples = 1000
mu = 0
var = 0
observed_sample_means = []
sample_mean = 0
num_bins = 50

while sample_size < 1:
    try:
        sample_size = int(input("Enter a sample size (>0): "))
    except ValueError:
        print("Sample size must be an integer > 0.")

while mu <= 0:
    try:
        mu = float(input("Enter a value for the population mean > 0: "))
    except ValueError:
        print("The population mean must be a floating point number > 0.")

var = mu**2

for i in range(num_samples):
    for k in range(sample_size):
        sample_mean += expovariate(1/mu)
    sample_mean /= sample_size
    observed_sample_means.append(sample_mean)
    sample_mean = 0

print("The observed sample mean was {}.".format(mean(observed_sample_means)))
print("The observed sample variance was {}.".format(variance(observed_sample_means)))
print("The theoretical mean is {}.".format(mu))
print("The theoretical variance is {}.".format(var/sample_size))

fig, ax = plt.subplots()
x, bins, patches = ax.hist(observed_sample_means, num_bins, density=True)
# plot theoretical pdf
y = ((1 / (np.sqrt(2 * np.pi) * np.sqrt(var/sample_size))) *
     np.exp(-0.5 * (1 / np.sqrt(var/sample_size) * (bins - mu))**2))
ax.plot(bins, y, '-')
ax.set_xlabel('Sample Means')
ax.set_ylabel('Relative Frequency')
ax.set_title('Relative Frequency Histogram')
plt.show()
