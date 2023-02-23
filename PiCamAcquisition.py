from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (800, 600)}))
picam2.set_controls({"ExposureTime":200, "FrameDurationLimits": (50,50), "AnalogueGain": 1})
picam2.start()

in1 = 17
in2 = 18
in3 = 27
in4 = 22
step_sleep = 0.02
step_count = 600
direction = True

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
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        if direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        time.sleep (step_sleep )
        if i%25==0:
            picam2.capture_file("/home/ponjaviclab/Downloads/StepperControl/02022023_capture/capthree"+str(i)+".tiff")
       
except KeyboardInterrupt:
    cleanup()
    exit(1)    

cleanup()
exit(0)
