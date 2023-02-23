from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time

# if the picamera2 is installed but you get the ImportError, run the following commands to make sure you have installed all dependencies.
#pip3 install opencv-python 
#sudo apt-get install libcblas-dev
#sudo apt-get install libhdf5-dev
#sudo apt-get install libhdf5-serial-dev
#sudo apt-get install libatlas-base-dev
#sudo apt-get install libjasper-dev 
#sudo apt-get install libqtgui4 
#sudo apt-get install libqt4-test

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (800, 600)}))
picam2.set_controls({"ExposureTime":200, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
picam2.start()

in1 = 17
in2 = 18
in3 = 27
in4 = 22
step_sleep = 0.02
step_count = 80 # 80 number of steps should covern a scan range of about 10 um. 
direction = True
directory = time.strftime("%Y%m%d-%H%M%S")+"_CL500mm_40X"
parent_dir = "/home/ponjaviclab/Downloads/" # depends on your system, you need to change this.
Acq_path = os.path.join(parent_dir, directory)
os.mkdir(Acq_path)
print("Directory '% s' is created" % Acq_path)

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )

motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0

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
            picam2.capture_file(Acq_path+filename)
       
except KeyboardInterrupt:
    cleanup()
    exit(1)    

cleanup()
exit(0)
