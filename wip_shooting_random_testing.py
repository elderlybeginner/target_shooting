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
		holes.append([random.randint(-5, 5), random.randint(-5, 5)])
	return holes

def calculate_centroid(holes):
	'''Calculating centroid (mean holes position: x, y) based on given points.'''
	x, y = zip(*holes)
	return (sum(x) / len(holes), sum(y) / len(holes))


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


def calculate_cp(tolerance, sd):
	'''Charts are the best to explain cp index. It's calculated as
	(USL - LSL) / (6*sigma).
	USL is Upper Specification Limit.
	LSL is Lower Specification Limit.
	(USL - LSL) is range of accepted values. Here it is equal to tolerance
	Six Sigma means six standard deviations.
	Sounds complicated, gets simple when you look for charts with
	indexes interpretation.'''
	return tolerance / (6 * sd)


def calculate_cpk(tolerance, sd, centroid):
	usl = tolerance / 2
	lsl = -(tolerance / 2)
	return min((usl - abs(complex(centroid[0], centroid[1])) / (3 * sd), abs(complex(centroid[0], centroid[1])) - lsl / (3 * sd)))


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


holes_amount = 10
tolerance = calibrate() # acceptable tolerance of shooting
holes = get_holes(holes_amount) 
centroid = list(calculate_centroid(holes))
print(f'centroid: x = {centroid[0]:.2f}; y = {centroid[1]:.2f}')
mean = calculate_mean(holes)
print('mean', mean)
sd = calculate_sd(holes, centroid)
print('sd = ', sd)
cp = calculate_cp(tolerance, sd)
print("Cp = ", cp)
cpk = calculate_cpk(tolerance, sd, centroid)
print("Cpk = ", cpk)

show_results(holes, centroid)
show_results_interpretation()
