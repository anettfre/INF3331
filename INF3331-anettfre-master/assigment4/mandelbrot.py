#!/usr/bin/python3

import mandelbrot_1 as mb1
import mandelbrot_2 as mb2
import mandelbrot_3 as mb3
import sys
import matplotlib.pyplot as plt
import numpy as np

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None):
	set = mb3.make_set(xmin, ymin, xmax, ymax, Nx, Ny, max_escape_time)
	if plot_filename != None:
		showImage(set, plot_filename)
	return set

def giveHelp():
	print("You can choose method or choose the region of the plane you want to draw in or choose the resolution or output filename")
	print("Choose method by writing mandelbrot_1, 2 or 3 after calling the program")
	print("Choose region og the plane by writing min1 min2 max1 max2 after calling the program")
	print("Choose the resolution by writing xresolution yresolution after calling the program, feks. python3 1000 1000")
	print("Choose output filename by writing the filename after calling the program")
	print("Choose method, region, resolution and outputfilename by writing all of them after calling the program")
	return 0

def showImage(set, filename):
	"""Take in a set to create a image of and a filename
	Saves the image with the  string filename
	"""
	m = plt.cm.magma_r
	m.set_under(color="black")
	plt.imshow(set, cmap=m, origin="lower", vmin=0.1)
	plt.savefig("filename")
	plt.show()

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "--help":
		giveHelp()
		sys.exit()

	elif len(sys.argv) == 5: #region of plane
		min1 = float(sys.argv[1])
		min2 = float(sys.argv[2])
		max1 = float(sys.argv[3])
		max2 = float(sys.argv[4])
		set = mb3.make_set(min1,min2,max1,max2)
		mb3.color(set)
		sys.exit()

	elif len(sys.argv) == 3: #resolution
		z1 = int(sys.argv[1])
		z2 = int(sys.argv[2])
		set = mb3.make_set(-1.5,-1.25,0.5,1.25, z1, z2)
		mb3.color(set)
		sys.exit()

	elif len(sys.argv) > 8: #all
		method = sys.argv[1]
		min1 = float(sys.argv[2])
		min2 = float(sys.argv[3])
		max1 = float(sys.argv[4])
		max2 = float(sys.argv[5])
		z1 = int(sys.argv[6])
		z2 = int(sys.argv[7])
		numberOfIerations = int(sys.argv[8])
		filename = sys.argv[9]
		set = method.make_set(min1, min2, max1, max2, z1, z2, numberOfIerations)
		sys.exit()


	if len(sys.argv) == 2: #method
		if sys.argv[1] == "mandelbrot_1":
			set = mb1.make_set(-1.5,-1.25,0.5,1.25)
			mb1.color(set)
		elif sys.argv[1] == "mandelbrot_2":
			set = mb2.make_set(-1.5,-1.25,0.5,1.25)
			mb2.color(set)
		elif sys.argv[1] == "mandelbrot_3":
			set = mb3.make_set(-1.5,-1.25,0.5,1.25)
			mb3.color(set)
		else: #filename
			set = mb3.make_set(-1.5,-1.25,0.5,1.25)
			showImage(set, sys.argv[1])
		sys.exit()

	else: #if no argument is given
		set = mb3.make_set(-1.5,-1.25,0.5,1.25)
		mb3.color(set)
		sys.exit()
