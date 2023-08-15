[![Docs](https://img.shields.io/badge/documentation-link-blueviolet)](https://AmirSTORMic/PiFocus/PiFocusDraft.md/)
[![Contributors](https://img.shields.io/github/contributors-anon/AmirSTORMic/PiFocus)](https://github.com/AmirSTORMic/PiFocus/graphs/contributors)
[![License](https://img.shields.io/github/license/AmirSTORMic/PiFocus?color=Green)](https://github.com/AmirSTORMic/PiFocus/blob/main/LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)
[![GitHub forks](https://img.shields.io/github/forks/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)

## Main Parts
  * [Laser (λ = 850 nm, CPS850, Thorlabs)](https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS850)
  * Relay lens pair
  * [Camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/)
  * [50/50 PBS](https://www.thorlabs.com/thorproduct.cfm?partnumber=CCM1-PBS255/M) (λ = 700-1300 nm)
  * Dichroic Mirror (12.5x17.6 mm, 800 nm, Shortpass Dichroic Mirror,	Edmund Optics	#69-196)
  * Objective Lenses
    - 100X/1.10 Water
    - 100X/1.35 Silicone
    - 60X/0.80
    - 20X/0.40 

## Scripts
Python scripts that have been used for hardware control, data acquisition, and analysis are available in this GitHub repository. The experimental data will be added soon.
  * PiFocusASI.py: To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * PiCamAcquisition.py: To acquire Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage.
  * [FECPlot.py](https://github.com/AmirSTORMic/PiFocus/master/FECPlot.py): To analyse the acquired datasets on the Autofocus system in the advanced lab. 

## Dependencies
Manage to get the MAX5216 SPI DAC to work with my Raspberry Pi.

`sudo apt-get install i2c-tools`

`pip3 install adafruit-blinka`

`sudo pip3 install adafruit-circuitpython-mcp4725`

Change the config file with: `sudo nano /boot/config.txt` and add the following lines to the end:

`dtparam=i2c_arm=on`

`dtparam=i2c1=on`

exit with ctrl-x and save with y.

Next need to enable the camera and I2C interface. Go to the Raspberry Pi terminal and type:

`sudo raspi-config` 

Then go to the interfacing options. Enable the camera and I2C.

If you want to detect the DAC to make sure it is connected. Run in the Raspberry Pi terminal:

`sudo i2cdetect -y 1`

In the Raspberry Pi terminal, run the following commands. 

`pip3 install opencv-python`


`sudo apt-get install libcblas-dev`


`sudo apt-get install libhdf5-dev`


`sudo apt-get install libhdf5-serial-dev`


`sudo apt-get install libatlas-base-dev`


`sudo apt-get install libjasper-dev`


`sudo apt-get install libqtgui4`


`sudo apt-get install libqt4-test`

## Issues
In the event that you come across any difficulties, please don't hesitate to file an issue and make sure to provide a thorough description of the problem.
