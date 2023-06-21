# πFocus

## About the project
The Ponjavic lab at the University of Leeds started PiFocus to provide a cost-effective, robust and easy-to-implement focus stabilisation system for optical microscopes. By creating a well-explained protocol, we hope to enable other laboratories to replicate this open-hardware focus stabilisation system.

The following students contributed to this project under the supervision of Dr Aleks Ponjavic:

- Robert Elliott
- Tabitha Cox
- Thomas Marsh
- Akhila Thamaravelil Abhimanue Achary
- Ziyun Wang
- Amir Rahmani

A detailed description of the contribution will be provided upon agreement between the group members.

## Introduction
For long-term image acquisition experiments, a reliable focus stabilisation system is required to prevent defocusing due to component drift. Thus, it would be desirable to maintain the sample in focus by utilising a focus stabilization technique. Considering that drift could occur in all three dimensions, lateral and axial drift need to be compensated simultaneously. In recent years, however, some developments have been made in the area of axial drift stabilization systems. 

## Method
The approach that we employ for this project relies upon developing microscopes that integrate not only the illumination and detection paths but also the optical focus stabilisation path. Our focus stabilization path relies on imaging and monitoring the change in the intensity profile of the IR laser beam reflected from the glass coverslip. Any change in the distance between the objective lens and the glass coverslip results in a lateral shift in the position of the returning beam, which is detected by the camera. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. A software-based feedback system detects this shift and corrects it by adjusting the position of the piezoelectric element built into the sample stage. By altering the intensity distribution of a back-reflected beam at the camera, this method reports defocusing value and direction when the axial position of the glass coverslip or imaging objective lens changes.

## Characterisation
  * Calibration Curve 
## Main Parts
  * [Laser (λ = 850 nm, CPS850, Thorlabs)](https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS850)
  * Relay lens pair
  * Camera
  * 50/50 Beam Splitter (λ = 300-1100 nm)
  * Dichroic Mirror (12.5x17.6 mm, 800 nm, Shortpass Dichroic Mirror,	Edmund Optics	#69-196)

## Codes
  * PiFocusASI.py: To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * PiCamAcquisition.py: To acquire Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage. 

## References:
  1. Bon, P., Bourg, N., Lécart, S. et al. Three-dimensional nanometre localization of nanoparticles to enhance super-resolution microscopy. Nat Commun 6, 7764 (2015). DOI: [10.1038/ncomms8764](https://doi.org/10.1038/ncomms8764)
  2. Rajdeep Chowdhury, Abhishek Sau, Jerry Chao, Ankith Sharma, and Siegfried M. Musser, "Tuning axial and lateral localization precision in 3D super-resolution microscopy with variable astigmatism," Opt. Lett. 47, 5727-5730 (2022) DOI: [10.1364/OL.466213](https://doi.org/10.1364/OL.466213)
  3. Hongqiang Ma and Yang Liu, "Embedded nanometer position tracking based on enhanced phasor analysis," Opt. Lett. 46, 3825-3828 (2021), DOI: [10.1364/OL.433740](https://doi.org/10.1364/OL.433740)
  4. Coelho, S., Baek, J., Walsh, J. et al. 3D active stabilization for single-molecule imaging. Nat Protoc 16, 497–515 (2021). DOI: [10.1038/s41596-020-00426-9](https://doi.org/10.1038/s41596-020-00426-9)
