import os
import cv2
import timeit
import cupy as cp
import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    
# Define the function that is going to be used to fit on the data. In our case, a 2D Gaussian profile. 
def TwoD_Gaussian(xdata, i0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  i0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()

try:
    from scipy.optimize import curve_fit
except ImportError:
    print("Unable to import curve_fit from scipy.optimize.")

from tkinter import Tk
from Tk.filedialog import askdirectory

Tk().withdraw()  # Prevents a full GUI window from appearing
folder_path = askdirectory()  # Show the folder selection dialog and return the selected folder path
print(f"Selected folder: {folder_path}")

import tifffile
import argparse

def main():
        parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--input', type = str, required = True)
        args = parser.parse_args()

        image = tifffile.imread(args.input)
        print('The data you are trying to analyse is: %s' % args.input)

        num_frames = image.shape[0]  # Assuming the frames are along the first dimension
        print(f"Number of frames: {num_frames}")

        x_sigma = []
        y_sigma = []
        
        im = np.asarray(img).astype(float)
        h1, w1 = im.shape
        x, y = np.meshgrid(np.arange(w1),np.arange(h1))
        
        popt, pcov = curve_fit(TwoD_Gaussian, (x, y), im.ravel(), p0=init_guess, maxfev = 150000)
        popt[3] = np.abs(popt[3])
        popt[4] = np.abs(popt[4])
        
        init_guess.clear()
        init_guess.append(popt)
        
        dd = TwoD_Gaussian((x,y),*popt)
        dd = dd.reshape(h1,w1)
        
        x_sigma.append(popt[3])
        y_sigma.append(popt[4])
        
        # plt.plot((popt[1],popt[1]+popt[3]),(popt[2],popt[2]))
        # plt.plot((popt[1],popt[1]),(popt[2],popt[2]+popt[4]))
        # plt.imshow(im)
        # plt.show()

        " To set the x-axis of the graph to the axial values "
        """ ------------------------------------------------------------------ """
        i_values = np.array(num_frames)
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

if __name__ == '__main__':
	    main()
