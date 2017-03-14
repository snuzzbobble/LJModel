"""
Module for user to create files with system information.

Cara Lynch
"""

import sys
import random


name = str(raw_input("Name of system: "))
N = int(raw_input("Number of particles in system as an integer: "))
m = float(raw_input("Mass of particles in system as a float: "))
rho = float(raw_input("Density of system as a float: "))
boxdim = (N/rho)**(1./3.)

# Open system file for writing
systemFile = open("system.in", "w")

systemFile.write(name + " " + str(N) + " " + str(m) + "\n")

for i in range (0, N):
    label = "p" + str(i)
    pos1 = random.uniform(0.0, boxdim)
    pos2 = random.uniform(0.0, boxdim)
    pos3 = random.uniform(0.0, boxdim)
    systemFile.write(label + " " + str(pos1) + " " + str(pos2) + " " + str(pos3) + " 0.0 0.0 0.0 \n")

systemFile.close()
