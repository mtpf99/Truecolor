import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt


# changes the values of each TIFF -- makes them lighter
def StdDev(x):
   return((x - (np.nanmean(x)-np.nanstd(x)*2))/((np.nanmean(x)+np.nanstd(x)*2) - (np.nanmean(x)-np.nanstd(x)*2)))


# open all tiffs and read them as numpy array, then assign to variable
# band 2
b2Path = gdal.Open('')
b2Array = np.array(b2Path.ReadAsArray())
# band 3
b3Path = gdal.Open('')
b3Array = np.array(b3Path.ReadAsArray())
# band 4
b4Path = gdal.Open('')
b4Array = np.array(b4Path.ReadAsArray())

# run through std dev function
# run each array through the min max function

b2 = StdDev(b2Array)
b3 = StdDev(b3Array)
b4 = StdDev(b4Array)

# create the trueColor
trueColor = np.dstack((b4, b3, b2))

plt.figure()
plt.imshow(trueColor)
plt.show()

