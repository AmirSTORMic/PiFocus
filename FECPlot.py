import os
import cv2
import time
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function that is going to be used to fit on the data. In our case, a 2D Gaussian profile. 
def gaussianbeam(xdata, i0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  i0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()

# Iterate directory to count the number of captures
def numFiles(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
        # print('File count:', count)
    return count

# This function applies the fitting algorithm on the beam profile and will give the calibration plots.
# In the following function, dLoc is the directory that the tif files are stored in.
# "init_guess" is an araye-like object to determine the initial guess for the parameters of the fiting function. 
# Beware that "scipy.optimize" is rather sensitive to the initial guess. 
# ScanRange is the range that over which the piezo stage is scanned to acquire the stacks.
# StepSize for the scanning
def FECPlot(dLoc, init_guess, ScanRange, StepSize):
    x_sigma = []
    y_sigma = []
    i_values = []
    dp = 'C:/Users/44785/'
    dir_Path = dp+dLoc
    count = numFiles(dir_Path)
    # init_guess = [1000,400,400,100,100,400]
    
    # To read the acquired images and apply the Gaussian fitting
    for i in range(1,count):
        i_values.append(i)
        stacks = dir_Path+'Test'+str(i).zfill(3)+'.tif'
        img = cv2.imread(stacks, -1)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        im = np.asarray(img).astype(float)
        #im = im[150:350, 300:500] # if you need to crop the images, uncomment this line. 
        
        h1, w1 = im.shape
        x, y = np.meshgrid(np.arange(w1),np.arange(h1))
        
        popt, pcov = curve_fit(gaussianbeam, (x, y), im.ravel(), p0=init_guess, maxfev = 150000)
        popt[3] = np.abs(popt[3])
        popt[4] = np.abs(popt[4])
        
        init_guess.clear()
        init_guess.append(popt)
        
        dd = gaussianbeam((x,y),*popt)
        dd = dd.reshape(h1,w1)
        
        x_sigma.append(popt[3])
        y_sigma.append(popt[4])
        
        # plt.plot((popt[1],popt[1]+popt[3]),(popt[2],popt[2]))
        # plt.plot((popt[1],popt[1]),(popt[2],popt[2]+popt[4]))
        # plt.imshow(im)
        # plt.show()

    " To set the x-axis of the graph to the axial values "
    """ ------------------------------------------------------------------ """
    i_values = np.array(i_values)
    z_values = i_values*StepSize
    z_values = z_values.tolist() # Based on a True/False direction
    
    "Standard Deviation Calculation"
    """ ------------------------------------------------------------------ """
    # See the link below for a reference of the standard deviation formula
    # https://www.mathsisfun.com/data/standard-deviation-formulas.html
    # Convert the lists to arrays
    x1 = np.asarray(x_sigma)
    y1 = np.asarray(y_sigma)
    
    DiffArr = y1 - x1
    
    # Calculate the mean of the values in your array
    mean_DiffArr = sum(DiffArr) / len(DiffArr)
    
    # Calculate the variance of the values in your array
    # This is 1/N * sum((x - mean(X))^2)
    var_DiffArr = sum((x - mean_DiffArr) ** 2 for x in DiffArr) / len(DiffArr)
    
    # Take the square root of the variance to get the standard deviation
    sd_XY = var_DiffArr ** 0.5
    print('This is the standard deviation:', sd_XY)
    
    "Plot the curves"
    """ ------------------------------------------------------------------ """
    # with plt.xkcd(): 
    plt.plot(z_values, x_sigma, 'ro', markerfacecolor='none', markersize=4, label="x width")
    plt.plot(z_values, y_sigma, 'bo', markerfacecolor='none', markersize=4, label="y width")
    plt.plot(z_values, np.subtract(x_sigma,y_sigma), 'ko', markerfacecolor='none', markersize=4)
    #slopeX, interceptX = np.polyfit(np.log(x_sigma), np.log(z_values), 1)
    #plt.text(.5, 80, r'$\sigma_y=10,\ \sigma_x=10$')
    plt.grid(True)
    plt.minorticks_on()
    plt.xlabel("Z Values (µm)")
    plt.ylabel("Beam Width (µm)")
    plt.legend()
    plt.title("dLoc")
    plt.show()
    
# Run the following commands to see the folders in the directory.
# dp = r'/Projects/Autofocus/'
# [x[0] for x in os.walk(dp)]

# FEC(dLoc, init_guess, ScanRange, StepSize)
# This will give the calibration curve for the dataset of interest.
