import sys
import os
from json import loads

import cv2
import numpy as np
from skimage.measure import compare_ssim as ssim

ERR_OK = 0
ERR_WA = 1
ERR_PE = 2
ERR_UH = 3

rootDir = os.path.dirname(os.path.abspath(__file__))
eps = 10e-3
maxPoint = 5
errweight = 10

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err


def compare(imgAnsPath, imgOutPath):
	x1 = cv2.imread(imgAnsPath)
	x2 = cv2.imread(imgOutPath)

	x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
	x2 = cv2.cvtColor(x2, cv2.COLOR_BGR2GRAY)

	#absdiff = cv2.absdiff(x1, x2)
	#cv2.imwrite(os.path.join(rootDir, "absdiff01.png"), absdiff)

	#diff = cv2.subtract(x1, x2)
	#result = not np.any(diff)

	m = mse(x1, x2)
	s = ssim(x1, x2)
	ds = (1 - s) / 2

	print("mse: %s, ssim: %s, dssim: %s" % (m, s, ds))

	if ds < eps:
		print(ds)
		exit(ERR_OK)
	else:
		print(max(int((1 - ds*errweight)*maxPoint), 0))
		exit(ERR_OK)



imgOut = sys.argv[2] # path to image
imgAns = sys.argv[3]

compare(imgAns, imgOut)