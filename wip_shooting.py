#!/usr/bin/env python3
''' '''


import math


def calibrate():
	'''Sets up ruller for measurements. Default value is 10 cm diameter.
	Two points should be marked as distance input.'''
	return(10)


def get_holes():
	'''Holes are marked. X, Y position of each hole is read.'''


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
	return min((usl - abs(complex(centroid[0], centroid[1])) / (3 * sd), abs(complex(centroid[0], centroid [1])) - lsl / (3 * sd)))


def show_results():
	pass


def show_results_interpretation():
	pass


calibrate()
get_holes()
holes = [[3, 4], [5, 8], [6, 7], [-3, 8], [-1, 0], [-2, 6], [2, 4]]

centroid = list(calculate_centroid(holes))
print(f'x = {centroid[0]:.2f}; y = {centroid[1]:.2f}')
mean = calculate_mean(holes)
print('mean', mean)
sd = calculate_sd(holes, centroid)
print(sd)
tolerance = 2  # acceptable tolerance of shooting
cp = calculate_cp(tolerance, sd)
print("Cp = ", cp)
cpk = calculate_cpk(tolerance, sd, centroid)
print("Cpk = ", cpk)

show_results()
show_results_interpretation()
