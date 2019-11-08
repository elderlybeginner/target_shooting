#!/usr/bin/env python3
''' '''


def calibrate():
	'''Sets up ruller for measurements. Default value is 10 cm diameter
	Two points should be marked as distance input'''
	return(10)


def get_holes():
	'''Holes are marked. X, Y position of each hole is read'''


def calculate_centroid(holes):
	'''Calculating centroid (mean holes position) based on given points'''
	x, y = zip(*holes)
	return (sum(x) / len(holes), sum(y) / len(holes))


def calculate_cp():
	'''Charts are the best to explain cp index. It's calculated as
	(USL - LSL) / (6*sigma).
	USL is Upper Specification Limit
	LSL is Lower Specification Limit
	(USL - LSL) is range of accepted values. Here it is equal to tolerance
	Six Sigma means six standard deviations
	Sounds complicated, gets simple when you look for charts with
	indexes interpretation'''
	pass


def calculate_cpk():
	usl = tolerance / 2
	lsl = -(tolerance / 2)


def show_results():
	pass


def show_results_interpretation():
	pass


calibrate()
get_holes()
holes = [[3, 4], [5, 8], [6, 7], [-3, 8], [-1, 0], [-2, 6], [2, 4]]

centroid = list(calculate_centroid(holes))
print(f'x = {centroid[0]:.2f}; y = {centroid[1]:.2f}')

tolerance = 2  # acceptable tolerance of shooting
calculate_cp()
calculate_cpk()

show_results()
show_results_interpretation()
