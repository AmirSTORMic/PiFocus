#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from picamera2 import Picamera2
import RPi.GPIO as GPIO

import board
import busio
import Adafruit-MCP4725 # pip install Adafruit-MCP4725

# ----------------------------------------------------------------------------------------------------
# Define the function that is going to be used to fit on the data. In our case, a 2D Gaussian profile.
# ----------------------------------------------------------------------------------------------------
def GaussianBeam(xdata, i0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  i0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()

# ----------------------------------------------------------------------------------------------------
# This function applies the fitting algorithm on the beam profile and will give the calibration plots.
# ----------------------------------------------------------------------------------------------------
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
        #im = im[150:350, 300:500]
        
        h1, w1 = im.shape
        x, y = np.meshgrid(np.arange(w1),np.arange(h1))
        
        popt, pcov = curve_fit(gaussianbeam, (x, y), im.ravel(), p0=init_guess, maxfev = 150000)
        popt[3] = np.abs(popt[3])
        popt[4] = np.abs(popt[4])
        
        init_guess.clear()
        init_guess.append(popt)
        
        dd = gaussianbeam((x,y),*popt)
        dd = dd.reshape(h1,w1)
        
        # plt.plot((popt[1],popt[1]+popt[3]),(popt[2],popt[2]))
        # plt.plot((popt[1],popt[1]),(popt[2],popt[2]+popt[4]))
        # plt.imshow(im)
        # plt.show()
        
        x_sigma.append(popt[3])
        y_sigma.append(popt[4])
        
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
    
    return np.subtract(x_sigma,y_sigma)
# ----------------------------------------------------------------------------------------------------
# A function to do a z scan using the Piezo
# ----------------------------------------------------------------------------------------------------
def ZPiezoCtrl(scanrange, step_size, direction, VDD):
    print("Scan range should be in um and step size should be in nm.")
    # DAC settings
    i2c = busio.I2C(board.SCL, board.SDA)
    MCP_DAC = adafruit_mcp4725.MCP4725(i2c)
    # Based on the spec sheet of the piezo driver, each 0.01V corresponds to 100 nm movements.
    V_step = (step_size*0.01)/100 
    StepValue = (V_step*4096)/VDD
    
    V_scan = ((scanrange/2)*0.01)/0.1
    ScanValue = (V_scan*4096)/VDD
    
    NumSteps = scanrange/(step_size*0.001)
    initPiezoposition = MCP_DAC.raw_value # get the MCP_DAC.raw_value
    StartingPoint = MCP_DAC.raw_value - ScanValue # set the MCP_DAC.raw_value to the starting point for the scan
    """
    Set the output voltage to specified value.  Value is a 12-bit number (0-4095) that is used to calculate the output voltage from:
          Vout =  (VDD*value)/4096
    I.e. the output voltage is the VDD reference scaled by value/4096. If persist is true it will save the voltage value in EEPROM 
    so it continues after reset (default is false, no persistence).
    """
    for i in range(1, NumSteps):
        MCP_DAC.raw_value = (MCP_DAC.raw_value + StepValue)
        time.sleep(1.0)
        
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
def AcqPiFocus(timepoints):
    directory = time.strftime("%Y%m%d-%H%M%S")
    parent_dir = "/home/ponjaviclab/" # depends on your system, you need to change this.
    Acq_path = os.path.join(parent_dir, directory)
    os.mkdir(Acq_path)
    print("Directory '% s' is created" % Acq_path)
    # setup picam capture
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (600, 400)}))
    picam2.set_controls({"ExposureTime":100, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
    picam2.start()
    for i in range(1, timepoints):
        filename = "Test"+str(i)+".tiff"
        picam2.capture_file(Acq_path+filename)
        FECPlot(Acq_path+filename, [2,370,370,380,380,150])
        if ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)>0)):
            ZPiezoCtrl(NumSteps, False)
        elif ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)<0)):
            ZPiezoCtrl(NumSteps, False)
        else:
            print("Focus is locked!")
