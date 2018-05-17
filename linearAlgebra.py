# -*- coding: utf-8 -*-

#Laura Davis 5 July 2017

#This program demonstrates NumPy's ability to solve linear equations
#The program must run in Anaconda's Spyder in order to use the numpy libraries 

import numpy
#Put your filepath to this .py file in cmd 
if __name__== '__main__':
	cmd = ("...linearAlgebra.py")

def main():

	n = 4
	A = numpy.zeros(n*n, float); A.shape = (n, n)		#matrix
	x = numpy.zeros(n, float)							#solution
	b = numpy.zeros(n, float)							#right-hand side

	#choose an x, set b=a*x, solve for y: A*y=b, and compare y with x
	for i in xrange(n):
		x[i] = i/2.0
		for j in xrange(n):
			A[i,j] = 2.0 + float(i+1)/ float(j+i+1)
	b = numpy.matmul(A, x)

	#solve linear ststem A*y=b:
	y = numpy.linalg.solve(A, b)

	#compare exact x with the y we computed:
	if abs(sum(x - y)) < 1.0E-10: print "correct solution", x, y
	else:
	#alternative
		if numpy.allclose(x, y, atol = 1.0E-10, rtol = 1.0E-12):
			print "correct solution", x, y
		else:
			print "wrong solution" , x, y
			
main()
	

