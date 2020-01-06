date: 2019-11-06, last modification 2020-01-05  
tags: [Python, shooting, sport shooting, precision, accuracy, measuring, statistics, gauss normal distribution]

# Measuring precision, accuracy and probability for Target Shooters

When shooting to target there are two main indicators of how good is your shooting:

1. Precision - the ability to hit the same place over and over. This gives you shot dispersion which I am going to measure with	a *standard deviation*.

![high precision](./img/highprecision.png)
Source: public domain

2. Accuracy - is the proximity of results to the center point. I am going to measure it with *centroid* (X,Y distance to the center)

![high accuracy](./img/highaccuracy.png)
Source: public domain

### The Project

The project is to calculate precision and accuracy based on bullet holes on target.  
You are scanning or a take photo of a target, mark holes (how about primary hole recognition?) and the program calculates **Centroid** (average position of all the holes) which is shown on the target and **Standard Deviation** (how far you are from the target in average). If you input your expectations (eg. 8 and up in the target), using standard deviation you will get the probability of hitting the target within that limit.

### Calculating centroid

Measurement is to be set as the distance from the center to the default place.  
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

### Calculating Standard Deviation and probability
TODO

### Visualization

The window is divided on two parts:

1. Setup / Data / Manage

![Program window](./img/window.png)

Setup is build of:

- calibrate: button for target calibration (diameter of the target)
- scan: imports scanned target (missed on the drawing)
- find holes: tries to mark holes automatically 
- fix holes: you can fix and enter holes by hand
- tolerance: dispersion you are trying to reach
- add text: any notes you would like to add
- date

Data is build of:

- Centroid: which gives info about your precision (X, Y: coordinates where is the middle of your shooting)
- Standard Deviation: which gives info about your accuracy
- Number of holes
- Probability: based on standard deviation, the probability that you shoot withing the tolerance

Stats are build of:

- save result
- load result
- stats: manage all your previous results 

2. Target or SD/Centroid (flipped by upper tabs)

In this window, you can flip between target view and history results.

### Data gathering

Standard deviation and centroid are gathered and put on the chart to show target shooting progress. 

I am a newbie in shooting, dispersion analysis and programming. Feel free to correct my mistakes and give some constructive tips.
