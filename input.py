"""
Module for user to create files with system information.

Cara Lynch
"""

import sys

name = str(raw_input("Name of system: "))
N = int(raw_input("Number of particles in system as an integer: "))
m = float(raw_input("Mass of particles in system as a float: "))

# Open system file for writing
systemFile = open("system.in", "w")

systemFile.write(name + str(N) + str(m) + "\n")

for i in range (0, N)
    label = "p" + str(i)
    systemFile.write(label + "0.0 0.0 0.0 0.0 0.0 0.0 \n")

systemFile.close()
