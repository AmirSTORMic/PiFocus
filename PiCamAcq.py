"""
This code is used to performe z-stack acquisition for a specific scan range using a step motor and Raspberry Pi camera. 
Authors: Tabitha Cox, Amir Rahmani, Aleks Ponjavic
Affiliation: School of Physics and Astronomy, University of Leeds, Leeds, UK
"""

from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time

# If the "picamera2" module is installed but you get the ImportError, make sure you have installed all dependencies.

# Camera settings
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (800, 600)}))
picam2.set_controls({"ExposureTime":200, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
picam2.start()

# The directory that the data should be saved in
direction = True
directory = time.strftime("%Y%m%d-%H%M%S")+"_"
parent_dir = "/home/ponjaviclab/Documents/" # depends on your system, you need to change this.
rootPath = os.path.join(parent_dir, directory)
os.mkdir(rootPath)
print("Directory '% s' is created" % rootPath)

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

# Check the connection on the Pi board to be exactly as it is here for the pins. 
in1 = 17
in2 = 18
in3 = 27
in4 = 22

motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0
step_sleep = 0.02
step_count = 80 # 80 number of steps should cover a scan range of about 100 um. 

GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()
    
try:    
    i = 0
    for i in range(step_count):
        filename = "Test"+str(i)+".tiff"
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        if direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        time.sleep (step_sleep )
        if i%5==0:
            picam2.capture_file(rootPath+filename)       
except KeyboardInterrupt:
    cleanup()
    exit(1)
cleanup()
exit(0)
