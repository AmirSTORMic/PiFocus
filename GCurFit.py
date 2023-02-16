# Import packages that are required for the analysis.
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

# 
def GCurFit(dir_path, init_guess, x1, ScanRange):
    x_sigma = []
    y_sigma = []
    i_values = []
    count = 0
    
    # Iterate directory to count the number of captures
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
        # print('File count:', count)
        
    # To read the acquired images and apply the Gaussian fitting
    for i in range(1,count):
        
        i_values.append(i)
        
        stacks = dir_path+'Test'+str(i)+'.tiff'
        img = cv2.imread(stacks)
        
        # This is just for images that need to be cropped for faster analysis.
        if x1!=0:
            img = crp_img
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        im = np.asarray(img).astype(float)
       
        t = time.time()
        
        h1, w1 = im.shape
        x, y = np.meshgrid(np.arange(w1),np.arange(h1))
        
        popt, pcov = curve_fit(gaussianbeam, (x, y), im.ravel(), p0=init_guess, maxfev = 10000)
        
        init_guess.clear()
        init_guess.append(popt)
        
        dd = gaussianbeam((x,y),*popt)
        dd = dd.reshape(h1,w1)
        
        x_sigma.append(popt[3])
        y_sigma.append(popt[4])
          
    # This is just to set the x-axis of the graph to the axial values
    StepSize = ScanRange/count
    i_values = np.array(i_values)
    z_values = i_values*StepSize
    z_values = z_values.tolist() # This should be based on True/False direction

    # Plot the curves        
    plt.plot(z_values, x_sigma, 'r*', markersize=4, label="x width")
    plt.plot(z_values, y_sigma, 'b*', markersize=4, label="y width")
    plt.plot(z_values, np.subtract(x_sigma,y_sigma), 'kx', markersize=4)
    #slopeX, interceptX = np.polyfit(np.log(x_sigma), np.log(z_values), 1)
    #plt.text(.5, 80, r'$\sigma_y=10,\ \sigma_x=10$')
    plt.grid(True)
    #plt.xlim(2, 5.5)
    # plt.title("Calibration Curve of Image Width (Astigmatic)")
    plt.xlabel("Z Values")
    plt.ylabel("Beam Profile Width")
    plt.legend()
    plt.show()
