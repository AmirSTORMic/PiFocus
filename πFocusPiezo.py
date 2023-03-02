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

__author__ = 'Amir Rahmani'
__version__ = '0.2.0'
__license__ = 'University of Leeds'
# -----------------------------------------------------------------------------
def gaussianbeam(xdata, i0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  i0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()
# -----------------------------------------------------------------------------
def GCurFit(dir_path, init_guess):
    x_sigma = []
    y_sigma = []
    i_values = []
    count = 0
    
    # Iterate directory to count the number of captures
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
        # print('File count:', count)
    
    # To read the acquired images and apply the Gaussian fitting
    for i in range(1,count):
        t = time.time()
        i_values.append(i)
        
        stacks = dir_path
        img = cv2.imread(stacks)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        im = np.asarray(img).astype(float)
        
        h1, w1 = im.shape
        x, y = np.meshgrid(np.arange(w1),np.arange(h1))
        
        popt, pcov = curve_fit(gaussianbeam, (x, y), im.ravel(), p0=init_guess, maxfev = 5000)
        
        init_guess.clear()
        init_guess.append(popt)
        
        dd = gaussianbeam((x,y),*popt)
        dd = dd.reshape(h1,w1)
        
        x_sigma.append(popt[3])
        y_sigma.append(popt[4])

    # Plot the curves        
    plt.plot(i_values, x_sigma, 'r*', markersize=4, label="x width")
    plt.plot(i_values, y_sigma, 'b*', markersize=4, label="y width")
    plt.plot(i_values, np.subtract(x_sigma,y_sigma), 'kx', markersize=4)
    
    plt.grid(True)
    
    plt.xlabel("Time")
    plt.ylabel("Beam Profile Width")
    plt.legend()
    plt.show()
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------    
def AcqPiFocus(timepoints):
    directory = time.strftime("%Y%m%d-%H%M%S")+"_CL500mm_40X"
    parent_dir = "/home/ponjaviclab/Downloads/" # depends on your system, you need to change this.
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
        GCurFit(Acq_path+filename, [2,370,370,380,380,150])
        if ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)>0)):
            StepperCtrl(NumSteps, False)
        elif ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)<0)):
            StepperCtrl(NumSteps, False)
        else:
            print("Focus is locked!")
