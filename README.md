# πFocus

## About the project
PiFocus is a project which was started in the Ponjavic lab at the University of Leeds to have a cost-effective, robust and easy-to-implement focus stabilisation system on our optical microscopes. We hope to be able to create a well-explained protocol for this open-hardware focus stabilisation system that can be easily duplicated by other laboratories.

The following students contributed to this project under the supervision of Dr Aleks Ponjavic:

- Robert Elliott
- Tabitha Cox
- Akhila Thamaravelil Abhimanue Achary
- Ziyun Wang
- Amir Rahmani

A detailed description of the contribution will be provided upon agreement between the group members.

## Introduction
Long image acquisition experiments require a reliable focus stabilisation system to avoid any defocusing resulting from the drift of components. In this regard, a form of focus stabilization in which the sample is maintained in focus is desirable. Since the drifts could be in all three dimensions, compensation for lateral and axial drift would be needed at the same time. However, there have been some developments for a focus stabilization system for axial drifts. 

## Method
The approach that we employ for this project relies upon developing microscopes that integrate not only the illumination and detection paths but also the optical focus stabilisation path. Our focus stabilization path relies on imaging and monitoring the change in the intensity profile of the IR laser beam reflected from the glass coverslip. Any change in the distance between the objective lens and the glass coverslip results in a lateral shift in the position of the returning beam, which is detected by the camera. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. A software-based feedback system detects this shift and corrects it by adjusting the position of the piezoelectric element built into the sample stage. By altering the intensity distribution of a back-reflected beam at the camera, this method reports defocusing value and direction when the axial position of the glass coverslip or imaging objective lens changes.

## Characterisation

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
