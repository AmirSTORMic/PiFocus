# =============================================================================
# Import Modules
# =============================================================================
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
import tifffile
import argparse
try:
    from scipy.optimize import curve_fit
except ImportError:
    print("Unable to import curve_fit from scipy.optimize.")
# =============================================================================
# Fitting function
# =============================================================================
# Define the function that is going to be used to fit on the data.
# In our case, a 2D Gaussian. 
def TwoD_Gaussian(xdata, I0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  I0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()

# =============================================================================
# Choose the data file
# =============================================================================
def choose_the_data_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select the data file:")
    if file_path:
        print(f"Data file: {file_path}")
        #filename = os.path.basename(file_path)
    else:
        raise IOError(f"No file selected!")
    root.destroy()
    return file_path

# =============================================================================
# Read the data
# =============================================================================
def read_data():
    filename = choose_the_data_file()
    data = tifffile.imread(filename)
    num_Slices = data.shape[0]
    h = data.shape[1]
    w = data.shape[2]
    x, y = np.meshgrid(np.arange(w),np.arange(h))
    for i in range(num_Slices):
        image = data[i,:,:]
        I0 = np.mean(data[i,0,0])
        init_guess = [I0, h/2, h/2, sX, sY, image.max()]
        x_sigma = []
        y_sigma = []
        popt, pcov = curve_fit(TwoD_Gaussian, (x, y), image.ravel(), p0=init_guess, maxfev = 150000)
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
    
        mean_DiffArr = sum(DiffArr) / len(DiffArr)
    
        # Calculate the variance of the values in your array
        # This is 1/N * sum((x - mean(X))^2)
        var_DiffArr = sum((x - mean_DiffArr) ** 2 for x in DiffArr) / len(DiffArr)
    
        # Take the square root of the variance to get the standard deviation
        sd_XY = var_DiffArr ** 0.5
        print('Optimized standard deviation:', sd_XY)
        
        # Error Handling for Division by Zero (if applicable)
        if len(DiffArr) == 0:
            print("Error: Division by zero encountered in variance calculation.")
            sd_XY = 0  # Default or error value
    
"Plot the curves"
""" ------------------------------------------------------------------ """
def plot_curves(z_values, x_sigma, y_sigma):
    try:
        from matplotlib import pyplot as plt
        plt.plot(z_values, x_sigma, 'ro', markerfacecolor='none', markersize=4, label="x width")
        plt.plot(z_values, y_sigma, 'bo', markerfacecolor='none', markersize=4, label="y width")
        plt.plot(z_values, np.subtract(x_sigma,y_sigma), 'ko', markerfacecolor='none', markersize=4)
        plt.grid(True)
        plt.minorticks_on()
        plt.xlabel("Z Values (µm)")
        plt.ylabel("Beam Width (µm)")
        plt.legend()
        plt.title("dLoc")
        plt.show()
    except ImportError:
        print("matplotlib is not installed.")
