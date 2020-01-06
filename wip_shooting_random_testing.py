#!/usr/bin/env python3
''' '''


import math
import matplotlib.pyplot as plt
import random


def calibrate():
	'''Sets up ruller for measurements. Default value is 10 cm diameter.
	Two points should be marked as distance input.'''
	return 10


def get_holes(amount):
	'''Holes are marked. X, Y position of each hole is read.'''
	holes = []
	for h in range(amount):
		holes.append([random.randint(-1, 2), random.randint(-2, 5)])
	return holes


def calculate_centroid(holes):
	'''Calculating centroid (mean holes position: x, y) based on given points.'''
	x, y = zip(*holes)
	return sum(x) / len(holes), sum(y) / len(holes)


def calculate_mean(holes):
	'''Calculate mean distance to the center. It's not the same as abs(complex(centroid[0], centroid[1])).'''
	total = 0
	for i in holes:
		total += abs(complex(i[0], i[1]))
	return total / len(holes)


def calculate_sd(holes, centroid):
	'''Calculate standard deviation.'''
	total = 0
	for i in holes:
		total += math.pow((abs(complex(i[0] - centroid[0], i[1] - centroid[1]))), 2)
	return math.sqrt(total / len(holes))


def calculate_probability(acceptable, mean, sd):
	'''Equitation for folded (half) normal distribution is different
	then for normal distribution. Probability calculation uses
	error function - math.erf() - to calculate probability.
	I still wonder if it should be calculated based on
	imaginary folded normal distribution. Providing the time
	it took me to go thru this statistic basics I think I would
	never finished it if I try to find solution with imagiary staff.
	Equitation for cumulative distribution (CDF) I have found on:
	https://arxiv.org/pdf/1402.3559.pdf and it is also on:
	https://infogalactic.com/info/Folded_normal_distribution'''
	go_for = 10 - acceptable
	prob1 = math.erf((go_for - mean) / (math.sqrt(2) * sd))
	prob2 = math.erf((go_for + mean) / (math.sqrt(2) * sd))
	prob = (prob1 + prob2) / 2
	return prob


def show_results(holes, centroid):
	circle = plt.Circle((0, 0), 1, color='k', fill=1, alpha=0.5)
	circle1 = plt.Circle((0, 0), 5, color='0.5', fill=0)
	circle2 = plt.Circle((0, 0), 10, color='k', fill=0)
	plt.gcf().gca().add_artist(circle)
	plt.gcf().gca().add_artist(circle1)
	plt.gcf().gca().add_artist(circle2)
	holes_ziped = zip(*holes)
	plt.scatter(*holes_ziped)
	plt.scatter(centroid[0], centroid[1], marker='+', c='r', edgecolor='k')
	plt.axis('scaled')
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	plt.show()


def show_results_interpretation():
	pass


acceptable = 5  # minimum target accepted (for probability)
holes_amount = 10
distance = calibrate()  # can be used for finding holes X, Y
holes = get_holes(holes_amount)
centroid = calculate_centroid(holes)
print('')
print('*' * 55)
print(f'Centroid: x = {centroid[0]:.2f}; y = {centroid[1]:.2f} (distance from center)')
mean = calculate_mean(holes)
print(f'Average points per shot: {10 - mean:.1f}')
sd = calculate_sd(holes, centroid)
print(f'Standard deviation: {sd:.2f}')
probability = calculate_probability(acceptable, mean, sd)
print('Probability hitting', acceptable, 'or more in the next shoot:', f'{probability * 100:.2f}%')
print('*' * 55, '\n')

show_results(holes, centroid)
