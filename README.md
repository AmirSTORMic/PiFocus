[![DOI:10.1101/2024.01.15.575442](http://img.shields.io/badge/DOI-10.1101/2024.01.15.575442-B31B1B.svg)](<https://doi.org/10.1101/2024.01.15.575442>)
[![Contributors](https://img.shields.io/github/contributors-anon/AmirSTORMic/PiFocus)](https://github.com/AmirSTORMic/PiFocus/graphs/contributors)
[![CC BY 4.0][cc-by-shield]][cc-by]
[![GitHub stars](https://img.shields.io/github/stars/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)
[![GitHub forks](https://img.shields.io/github/forks/AmirSTORMic/PiFocus?style=social)](https://github.com/AmirSTORMic/PiFocus/)


# PiFocus: Acquisition, Analysis and Hardware Control
<p align="justify">
The purpose of this repository is to provide a practical, step-by-step approach to doing your own focus stabilisation based on PiFocus technique. Specifically, you will find a method to set up the Raspberry Pi 4 (Model B), 16-bit DAC (AD5693, Adafruit), and 10-bit Raspberry Pi camera (Arducam OV9782). As part of our implementation, we will touch on the uses of different cameras as avenues into the adoptation of PiFocus. 
</p>

## Set the Raspberry Pi and Camera
Manage to get the MAX5216 SPI DAC to work with the Raspberry Pi.

```
sudo apt-get install i2c-tools
pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-mcp4725
```

Change the config file with: `sudo nano /boot/config.txt` and add the following lines to the end:

```
dtparam=i2c_arm=on
dtparam=i2c1=on
```

exit with ctrl-x and save with y.

Next need to enable the camera and I2C interface. Go to the Raspberry Pi terminal and type:

```
sudo raspi-config
```

Then go to the interfacing options. Enable the camera and I2C.

If you want to detect the DAC to make sure it is connected. Run in the Raspberry Pi terminal:

```
sudo i2cdetect -y 1
```

To install opencv-python:
```
suod apt install python3-opencv
```
or if you need to downgrade opencv:

```
pip3 install git+https://github.com/opencv/opencv-python
```

In the Raspberry Pi terminal, run the following commands:

```
sudo apt-get install libcblas-dev
```

```
sudo apt-get install libhdf5-dev
```

```
sudo apt-get install libhdf5-serial-dev
```

```
sudo apt-get install libatlas-base-dev
```

```
sudo apt-get install libjasper-dev
```

```
sudo apt-get install libqtgui4
```

```
sudo apt-get install libqt4-test
```


## Codes
Python scripts that have been used for hardware control, data acquisition, and analysis are available in this GitHub repository. The experimental data will be added soon.
  * [PiFocusASI](https://github.com/AmirSTORMic/PiFocus/master/PiFocusASI.py): To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * [PiFocusPCP](https://github.com/AmirSTORMic/PiFocus/master/PiFocusPCP.py): To acquire Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage.

## Issues
In the event that you come across any difficulties, please don't hesitate to file an issue and make sure to provide a thorough description of the problem.

## License
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
