#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Amir Rahmani
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time
import os

from picamera2 import Picamera2
import RPi.GPIO as GPIO
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
    
    # This is just to set the x-axis of the graph to the axial values
    #StepSize = ScanRange/count
    #i_values = np.array(i_values)
    #z_values = i_values*StepSize
    #z_values = z_values.tolist() # This should be based on True/False direction
    
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
def StepperCtrl(NumSteps, defocusDir):
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    step_sleep = 0.02
    step_count = NumSteps # We need to calculate it based on the amount that the stage should defocus to correct the axial drift
    direction = defocusDir

    step_sequence = [[1,0,0,1],
                    [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1]]

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

    motor_pins = [in1,in2,in3,in4]
    motor_step_counter = 0
    
    try:    
        i = 0
        for i in range(step_count):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin])
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            if direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            time.sleep (step_sleep)
            
        except KeyboardInterrupt:
        cleanup()
        exit(1)    

    cleanup()
    exit(0)
# -----------------------------------------------------------------------------
def cleanup():
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()
# -----------------------------------------------------------------------------    
def AcqPiFocus(timepoints):
    # setup picam capture
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (600, 400)}))
    picam2.set_controls({"ExposureTime":100, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
    picam2.start()
    AcqPath = "/home/ponjaviclab/Downloads/StepperControl/"+time.strftime("%Y%m%d-%H%M%S")+"_Lens/
    for i in range(1, timepoints):
        picam2.capture_file(AcqPath+"Test"+str(i)+".tiff")
        GCurFit(AcqPath+"Test"+str(i)+".tiff", [2,370,370,380,380,150])
        if ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)>0)):
            StepperCtrl(NumSteps, False)
        elif ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)<0)):
            StepperCtrl(NumSteps, False)
        else:
            print("Focus is locked!")
