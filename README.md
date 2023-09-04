[![Docs](https://img.shields.io/badge/documentation-link-blueviolet)](https://github.com/AmirSTORMic/piFocus/blob/main/PiFocusDraft.md)
[![Contributors](https://img.shields.io/github/contributors-anon/AmirSTORMic/PiFocus)](https://github.com/AmirSTORMic/PiFocus/graphs/contributors)
[![License](https://img.shields.io/github/license/AmirSTORMic/PiFocus?color=Green)](https://github.com/AmirSTORMic/PiFocus/blob/main/LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)
[![GitHub forks](https://img.shields.io/github/forks/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)

# PiFocus: A universal focus stabilization approach using astigmatism
<p align="justify">
In this repository, you'll find a semi protocol detailing the process for setting up the PiFocus system. The collection encompasses designs, hardware specifications, and software components that are all listed below. Additionally, there are scripts available for replicating calibration outcomes, along with the necessary Python code for conducting autofocus operations and a Beanshell script to perform autofocusing through MicroManager. For a comprehensive understanding of the entire project, please refer to the provided documentation link.
</p>

## Set the Raspberry Pi and Camera
Manage to get the MAX5216 SPI DAC to work with the Raspberry Pi.

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

## Optomechanics and Optics
  * [Laser: 880 nm, 3 mW, Laser Diode, FC/PC](https://www.thorlabs.com/thorproduct.cfm?partnumber=LP880-SF3)
  * [FC/PC Fiber Adapter with External SM1](https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1FC)
  * [L1: f = 200.0 mm, Ø1" Achromatic Doublet, ARC: 650 - 1050 nm](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-200-B)
  * [L2: f = 80.0 mm, Ø1" Achromatic Doublet, ARC: 650 - 1050 nm](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-080-B)
  * [L3: f = 500.0 mm, Ø1", N-BK7 Mounted Plano-Convex Round Cyl Lens](https://www.thorlabs.com/thorproduct.cfm?partnumber=LJ1144RM)
  * [L4: f = 200.0 mm, Ø1" Achromatic Doublet, ARC: 650 - 1050 nm](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-200-B)
  * [Ø1/2" Mounted Achromatic Quarter-Wave Plate, Ø1" Mount, 690 - 1200 nm](https://www.thorlabs.com/thorproduct.cfm?partnumber=AQWP05M-980)
  * [Camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/)
  * [Cube-Mounted PBS](https://www.thorlabs.com/thorproduct.cfm?partnumber=CCM1-PBS255/M)
  * Dichroic Mirror (12.5x17.6 mm, 800 nm, Shortpass Dichroic Mirror,	Edmund Optics	#69-196)
  * Objective Lenses
    - 100X/1.35 Silicone
    - 100X/1.10 WI
    - 60X/1.27 WI
    - 40X/0.60 Air
    - 20X/0.40 Air

## Codes
Python scripts that have been used for hardware control, data acquisition, and analysis are available in this GitHub repository. The experimental data will be added soon.
  * [PiFocusASI](https://github.com/AmirSTORMic/PiFocus/master/PiFocusASI.py): To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * [PiFocusPCP](https://github.com/AmirSTORMic/PiFocus/master/PiFocusPCP.py): To acquire Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage.
  * [FECPlot](https://github.com/AmirSTORMic/PiFocus/master/FECPlot.py): To analyse the acquired datasets on the Autofocus system in the advanced lab. 

## Issues
In the event that you come across any difficulties, please don't hesitate to file an issue and make sure to provide a thorough description of the problem.
