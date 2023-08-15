"""
This code is used to performe z-stack acquisition for a specific scan range on the implemented focus stabilisation system with the ASI camera and CoreMorrow piezo stage. 
Authors: Amir Rahmani, Aleks Ponjavic
Affiliation: School of Physics and Astronomy, University of Leeds, Leeds, UK
"""

# Import packages that are required for the analysis.
import os
import cv2
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import argparse
import zwoasi as asi # pip install zwoasi

# env_filename = os.getenv('PiFocus_ASI')

# Define the function that is going to be used to fit on the data. In our case, a 2D Gaussian profile. 
def gaussianbeam(xdata, i0, x0, y0, sX, sY, amp):
    (x, y) = xdata
    x0 = float(x0)
    y0 = float(y0)
    eq =  i0+amp*np.exp(-((x-x0)**2/2/sX**2 + (y-y0)**2/2/sY**2))
    return eq.ravel()

# -----------------------------------------------------------------------------
def GCurFit(pathRoot, init_guess):
    x_sigma = []
    y_sigma = []
    i_values = []
    count = 0
    
    # Iterate directory to count the number of captures
    for path in os.listdir(pathRoot):
        # check if current path is a file
        if os.path.isfile(os.path.join(pathRoot, path)):
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
def AcqPiFocus(timepoints, TestNum):
    if TestNum.isdigit():
        print("This is test #"+str(TestNum))
    else:
        print("Enter an integer for the test number.")
    AcqPath = "/home/ponjaviclab/Documents/"+time.strftime("%Y%m%d-%H%M%S")+"_Test"+str(TestNum)+"/"
    num_cameras = asi.get_num_cameras()
      if num_cameras == 0:
      print('No cameras found')
      sys.exit(0)
    cameras_found = asi.list_cameras()  # Models names of the connected cameras
    if num_cameras == 1:
        camera_id = 0
        print('Found one camera: %s' % cameras_found[0])
    else:
        print('Found %d cameras' % num_cameras)
        for n in range(num_cameras):
            print('    %d: %s' % (n, cameras_found[n]))
        # TO DO: allow user to select a camera
        camera_id = 0
        print('Using #%d: %s' % (camera_id, cameras_found[camera_id]))
        
    camera = asi.Camera(camera_id)
    camera_info = camera.get_camera_property()
    
    # Get all of the camera controls
    print('')
    print('Camera controls:')
    controls = camera.get_controls()
    for cn in sorted(controls.keys()):
        print('    %s:' % cn)
        for k in sorted(controls[cn].keys()):
            print('        %s: %s' % (k, repr(controls[cn][k])))    
    # Use minimum USB bandwidth permitted
    camera.set_control_value(asi.ASI_BANDWIDTHOVERLOAD, camera.get_controls()['BandWidth']['MinValue'])
    
    # Set some sensible defaults. They will need adjusting depending upon
    # the sensitivity, lens and lighting conditions used.
    camera.disable_dark_subtract()

    camera.set_control_value(asi.ASI_GAIN, 150)
    camera.set_control_value(asi.ASI_EXPOSURE, 15000)
    camera.set_control_value(asi.ASI_WB_B, 99)
    camera.set_control_value(asi.ASI_WB_R, 75)
    camera.set_control_value(asi.ASI_GAMMA, 50)
    camera.set_control_value(asi.ASI_BRIGHTNESS, 50)
    camera.set_control_value(asi.ASI_FLIP, 0)
    
    print('Enabling stills mode')
    try:
        # Force any single exposure to be halted
        camera.stop_video_capture()
        camera.stop_exposure()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        pass

    print('Capturing a single 16-bit mono image')
    filename = 'image_mono.tiff'
    camera.set_image_type(asi.ASI_IMG_RAW16)
    camera.capture(filename=filename)
    print('Saved to %s' % filename)
    save_control_values(filename, camera.get_control_values())
    
    # Enable video mode
    try:
        # Force any single exposure to be halted
        camera.stop_exposure()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        pass
    
    for i in range(1, timepoints):
        print('Capturing a single 16-bit mono frame')
        filename = 'Test'+str(i)+'.tiff'
        camera.set_image_type(asi.ASI_IMG_RAW16)
        camera.capture_video_frame(filename=filename)
        # Apply the fiiting algorithm to the frame that just captured
        GCurFit(AcqPath+filename, [2,370,370,380,380,150])
        if ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)>0)):
            StepperCtrl(NumSteps, False)
        elif ((np.subtract(x_sigma,y_sigma)>10) and (np.subtract(x_sigma,y_sigma)<0)):
            StepperCtrl(NumSteps, False)
        else:
            print("Focus is locked!")
