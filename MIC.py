"""
Method implementing the minimum image convention for the separation between two particles

Cara Lynch

07/02/2017
"""

import numpy as np

from Particle3D import Particle3D as P

def vecsep(p1,p2,L):
	"""
	Calculate the relative vector separation of two particles 1 and 2 according to the minimum image convention.

	:param p1: particle 1 represented as a Particle3D instance
	:param p2: particle 2 represented as a Particle3D instance
	:param L: simulation box length
	:return: MIC vector separation of particles represented by a (1,3) Numpy array
	"""

	# Compute vector separation of the two particles
	vecsep = P.vectorseparation(p1,p2)
	print vecsep
	position2 = p2.position
	
	# Test each component of the vector separation
	for i in range(0,3):
		#Test if the separation is bigger than half a box length
		while abs(vecsep[i]) > L/2 :
			#If the separation is negative, then the image will be -L/2 in the direction considered
			if vecsep[i] < 0:
				position2[i] = p2.position[i] - L/2
				vecsep[i] = p1.position[i] - position2[i]
			
			#If the separation is positive, then the image will be +L/2 in the direction considered
			else:
				position2[i] = p2.position[i] + L/2
				vecsep[i] = p1.position[i] - position2[i]
	
	#Returns the MIC vector separation as a (1,3) Numpy array
	return vecsep
