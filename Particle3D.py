"""
A class representing a particle moving in 3D space, complete with various methods.

Authors: Marina Ruiz-Sanchez-Oro, Cara Lynch

Date: 08/11/2016

"""

import numpy as np

class Particle3D(object) :

    # Initialise a Particle3D instance
    def __init__(self, label, x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, mass):
	"""
	Initialise a Particle3D instance
	
	:param label: label of the particle as a string
	:param x_pos, y_pos, z_pos: position coordinates of the particle as floats
	:param x_vel, y_vel, z_vel: velocity coordinates of the particle as floats
	:param mass: mass of the particle as a float
	"""
	self.label = label
        self.position = np.array([x_pos, y_pos, z_pos])
        self.velocity = np.array([x_vel, y_vel, z_vel])
        self.mass = mass

    # Formatted output as string
    def __str__(self):
	"""
	Print the label and position coordinates of the particle

	:param Particle3D: Particle3D instance
	:return: formatted output as string with label and position coordinates
	"""
        return  str(self.label) + str(self.position)
 

    # Kinetic energy
    def kineticEnergy(self):
	"""
	Return the kinetic energy of the particle
	
	:param Particle3D: Particle3D instance
	:return: kinetic energy as particle as float
	"""
        return 0.5*self.mass*np.inner(self.velocity,self.velocity)

    # Time integration methods
    # First-order velocity update
    def leapVelocity(self, dt, force):
	"""
	Update the velocity to the first order

	:param Particle3D: Particle3D instance
	:param dt: timestep as float
	:param force: force as a vector represented by a (1,3) Numpy array
	:return: updated velocity of particle represented by a (1,3) Numpy array
	"""
        self.velocity = self.velocity + dt*force/self.mass

    # First-order position update
    def leapPos1st(self, dt):
	"""
	Update the position to the first order
	
	:param Particle3D: Particle3D instance
	:param dt: timestep as float
	:return: first order update of position of particle represented by a (1,3) Numpy array
	"""
        self.position = self.position + dt*self.velocity

    # Second-order position update
    def leapPos2nd(self,dt,force):
	"""
	Update the position to the second order
	
	:param Particle3D: Particle3D instance
	:param dt: timestep as float
	:param force: force as a vector represented by a (1,3) Numpy array
	:return: second order update of position of particle represented by a (1,3) Numpy array
	"""
        self.position = self.position + dt*self.velocity + 0.5*dt**2*force/self.mass

    # Create a particle from a file entry
    @staticmethod
    def createparticle(fileIn):
	"""
	Create a particle from a file entry which has the label of the particle and its mass in the first line, the position coordinates of the particle in the second line and the velocity coordinates of the particle in the third line

	:param fileIn: file opened for reading
	:return: Particle3D as an instance
	"""
        line1 = fileIn.readline()
        labelmass = list(line1.split())
        label = str(labelmass[0])
        mass = float(labelmass[1])
	print str(mass)
        line2 = fileIn.readline()
        position = list(line2.split())
        x_pos = float(position[0])
        y_pos = float(position[1])
        z_pos = float(position[2])
	print str(z_pos)
        line3 = fileIn.readline()
        velocity = list(line3.split())
        x_vel = float(velocity[0])
        y_vel = float(velocity[1])
        z_vel = float(velocity[2])
        return Particle3D(label, x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, mass)

    # Relative vector separation of two particles
    @staticmethod
    def vectorseparation(p1, p2):
	"""
	Calculate the relative vector separation of two particles 1 and 2

	:param p1: particle 1 represented as a Particle3D instance
	:param p2: particle 2 represented as a Particle3D instance
	:return: vector separation of particles represented by a (1,3) Numpy array
	"""
        return p1.position - p2.position
