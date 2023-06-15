"""
This code is used to performe z-stack acquisition for a specific scan range on the implemented focus stabilisation system using the CoreMorrow piezo stage. 
"""

__author__ = 'Amir Rahmani, Aleks Ponjavic'
__version__ = '1.0.0'
__license__ = 'University of Leeds'

import busio
import board
import adafruit_mcp4725

import os
import sys
import time
import math
import timeit
import datetime

from picamera2 import Picamera2
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray

# Camera settings
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (800, 600)}))
picam2.set_controls({"ExposureTime":200, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
picam2.start()

# -----------------------------------------------------------------------------
def PiPiezoAcq(scanrange, step_size, VDD):
    print("Scan range should be in um and step size should be in nm.")
    # DAC settings
    i2c = busio.I2C(board.SCL, board.SDA)
    MCP_DAC = adafruit_mcp4725.MCP4725(i2c)
    # Based on the spec sheet of the piezo driver, each 0.01V corresponds to 100 nm movements.
    V_step = (step_size*0.01)/100 
    StepValue = (V_step*4096)/VDD
    StepValue = round(StepValue)
    
    V_scan = ((scanrange/2)*0.01)/0.1
    ScanValue = (V_scan*4096)/VDD
    
    NumSteps = int(scanrange/(step_size*0.001))
    initPiezoposition = float(MCP_DAC.raw_value) # get the MCP_DAC.raw_value
    print("The Z stage is at"+str(initPiezoposition))
    
    StartingPoint = float(MCP_DAC.raw_value) - ScanValue # set the MCP_DAC.raw_value to the starting point for the scan
    print(StartingPoint)
    MCP_DAC.raw_value = round(StartingPoint)
    print("The starting point for the scanning is "+str(MCP_DAC.raw_value))
    """
    Set the output voltage to specified value.  Value is a 12-bit number (0-4095) that is used to calculate the output voltage from:
          Vout =  (VDD*value)/4096
    I.e. the output voltage is the VDD reference scaled by value/4096. If persist is true it will save the voltage value in EEPROM 
    so it continues after reset (MCP_DAC.raw_valuedefault is false, no persistence).
    """
    # Acquisition directory
    directory = time.strftime("%Y%m%d_%H%M%S")+"_TL200mmCL500mm_40X"
    parent_dir = "/home/ponjaviclab/Documents/" # depends on your system, you need to change this.
    Acq_path = os.path.join(parent_dir, directory)
    os.mkdir(Acq_path)
    print("Directory '% s' is created" % Acq_path)
    
    for i in range(1, NumSteps):
        filename = "Test"+str(i)+".tiff"
        picam2.capture_file(Acq_path+"/"+filename)
        MCP_DAC.raw_value = MCP_DAC.raw_value + StepValue
        if MCP_DAC.raw_value >= 4095:
            MCP_DAC.raw_value = MCP_DAC.raw_value - 2*ScanValue
            print("Piezo is out of range.")
        time.sleep(0.1)
        print("Axial scanning is running. Z position is "+str(MCP_DAC.raw_value))
