import numpy as np
import vaex as vx
import numexpr as ne
import vaex.multithreading as mt
import timeit
import math
import vaex.execution
import threading
lock = threading.Lock()
import sys
import pandas as pd
pd.Series

pool = mt.pool
ds = vx.open("data/Aq-A-2-999-shuffled-10percent.hdf5") if len(sys.argv) == 1 else sys.argv[1]
ds.set_fraction(0.1)
ds.select_expression("x>58")
x = ds("x**2")
#xlim = x.minmax()
#print xlim

expr = ds("x", "y")
print "means", expr.mean()
expr = expr.masked()
print "means", expr.mean()
#dsa
#import theano.tensor as T
#from theano import function
##x = T.dvector('x')
#z = eval("x**2")
#func = function([x], z)

#print "total", expr.sum()
means = expr.mean()
#vars = expr.var()
stds = [var_central**0.5 for var_central in expr.var(means=means)]
print "means", means, means * len(ds)
#print "vars", vars, vars**0.5
print "stds", stds

limits = expr.minmax()
std = np.mean(stds)
limits = zip(means-3*std, means+3*std)
grid = expr.histogram(limits, 256)
import pylab
expr.plot(np.log10(grid), limits-means.reshape(2,1))
x, y = means
#pylab.scatter(x, y)
pylab.show()
sys.exit(0)

s = pd.Series(ds.columns["x"])
if 1:
	def case_a():
		#return expr.minmax()
		return expr.mean()

	print "limits", case_a()

	def case_b():
		return vx.execution.main_manager.find_min_max(ds, [expr.expressions[0]])[0], vx.execution.main_manager.find_min_max(ds, [expr.expressions[1]])[0]
		#vx.execution.main_manager.execute()

	print "limits", case_b()
	N = 10
	print "case_a", timeit.timeit("case_a()", number=N, setup="from __main__ import case_a")/N
	print "case_b", timeit.timeit("case_b()", number=N, setup="from __main__ import case_b")/N


limits = expr.minmax()

def case_a():
	return expr.histogram(limits=limits)

grid = case_a()
N = 10
print "case_a", timeit.timeit("case_a()", number=N, setup="from __main__ import case_a")/N
dsa
import pylab
print "histogram", grid, grid.max()
pylab.imshow(np.log(grid))
pylab.show()

def case_bh():
	return vx.execution.main_manager.find_min_max(ds, [expr.expressions[0]])[0], vx.execution.main_manager.find_min_max(ds, [expr.expressions[1]])[0]
	#vx.execution.main_manager.execute()

print "limits", case_b()
print "case_b", timeit.timeit("case_b()", number=N, setup="from __main__ import case_b")/N
