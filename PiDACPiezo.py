import board
import busio
import adafruit_mcp4725

# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize MCP4725.
dac = adafruit_mcp4725.MCP4725(i2c)

dac.value = 65535

dac.raw_value = 4095

dac.normalized_value = 1.0
try:    
    i = 0
    for i in range(step_count): #The range of values for step_count is 0 (minimum/ground) to 4095 (maximum/Vout).
        dac.raw_value = i
    # Go back down the 12-bit raw range.
    # print("Going down 3.3-0V...")
    # for i in range(4095, -1, -1):
        # dac.raw_value = i
    except KeyboardInterrupt:
    exit(1)
exit(0)    
