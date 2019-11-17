date: 2019-11-06  
tags: [Python, shooting, sport shooting, Cp, Cpk, process capability index, precision, accuracy, measuring]

# Cp and Cpk for Target Shooters

When shooting to target there are two main indicators how good is your shooting:

1. Precision - the ability to hit the same place over and over. This gives you shot dispersion which I am going to measure with	 Cp index

![high precision](./img/highprecision.png)
Source: public domain

2. Accuracy - is the proximity of results to the center point. I am going to measure it with Cpk index

![high accuracy](./img/highaccuracy.png)
Source: public domain

### The Project

The project is to calculate precision and accuracy based on bullet holes on target.  
You are scanning or take photo of a target, mark holes (how about primary hole recognition?) and program calculates Cp and Cpk for you. **Centroid** (average position of all the holes) is shown on the target.

### Cp and Cpk

TODO

### Calculating centroid

Measurement is to be set as the distance from the center to default place.  
Then we calculate holes position as a list of lists: 

h1 = [x, y], h2 = [x, y], ... hn = [x,y]  
h2 = ...  
...    
hn = ...  

holes = [h1, h2, ..., hn]

and centroid is calculated:

```python
x = [h[0] for h in holes]
y = [h[1] for h in holes]  #  or x, y = zip(*holes)

centroid = [sum(x) / len(holes), sum(y) / len(holes)]
```

### Calculating Cp and Cpk

*Cp:*

(USL - LSL) / (6 * sigma).  
USL is Upper Specification Limit.  
LSL is Lower Specification Limit.  
(USL - LSL) is range of accepted values. Here it is equal to tolerance  
Six Sigma means six standard deviations.  

(math equitation should be here)

*Cpk:*

(math equitation instead of code here)

```python
def calculate_cpk(tolerance, sd, centroid):
    usl = tolerance / 2 
    lsl = -(tolerance / 2)
    return min((usl - abs(complex(centroid[0], centroid[1])) / (3 * sd), abs(complex(centroid[0], centroid[1])) - lsl / (3 * sd)))
```

*6 * sigma:*

I made approximation that sigma is standard deviation, thus it is calculated as:
(math equitation will be here instead of code): 

```python
total = 0
for i in holes:
	total += math.pow((abs(complex(i[0] - centroid[0], i[1] - centroid[1]))), 2)
sixsigma =  math.sqrt(total / len(holes))
```	

### Visualization

Centroid is marked on target. Cp and Cpk are shown.

### Data gathering

Cp and Cpk are gather and put on chart to show target shooting progress. 

I am newbie in shooting, dispersion analysis and programming. Feel free to correct my mistakes and give some constructive tips.

