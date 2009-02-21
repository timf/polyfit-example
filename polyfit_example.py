#!/usr/bin/env python

# Sample polyfit
# timfreeman.org

from pylab import *
import math

ylabel_text = "seconds"
xlabel_text = "N"
TITLE="Response times"

# data:
y = [1.090, 1.650, 3.312, 5.274, 12.985, 23.433]
x = [1, 2, 4, 8, 16, 32]

ZOOMOUT=True
x1or2 = x
if ZOOMOUT:
    x1or2 = [1, 2, 4, 8, 16, 32, 64]

def fact(x):
    if x==0:
        return 1
    else:
        return x * fact(x-1)

m, b = polyfit( x , y , 1)
print "m: %.3f" % m
print "b: %.3f" % b

y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []

for xval in x1or2:
    y2.append(xval * m + b)
    y3.append(math.log(xval) + b)
    y4.append(xval + b)
    y5.append(math.log(xval) * xval + b)
    y6.append(xval*xval + b)
    y7.append(xval*xval*xval + b)
    y7.append(fact(xval) + long(b))

plot(x, y, 'bo', linewidth=2, label='data')
plot(x1or2, y2, ':k', linewidth=2, label='polyfit')
plot(x1or2, y3, '-g', linewidth=1, label='log(n)')
plot(x1or2, y4, '-r', linewidth=1, label='linear')
#plot(x1or2, y5, '-b', linewidth=1, label='n log(n)')
#plot(x1or2, y6, '-y', linewidth=1, label='quadratic')
#plot(x1or2, y7, '-b', linewidth=1, label='n^3')
#plot(x1or2, y7, '-b', linewidth=1, label='factorial')

xlabel("N")
ylabel(ylabel_text)

grid(True)

axis(xmax=x1or2[-1] + 2)

legend(loc=2)
title(TITLE + ", constant=%.2f" % b)

figname = "result.png"
savefig(figname)
print "wrote %s" % figname
