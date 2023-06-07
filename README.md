# πFocus

## About the project
PiFocus is a project which was started in the Ponjavic lab at University of Leeds with the goal of having a cost-effective, robust and easy-to-implement focus stabilisation system on our optical microscopes. We hope to be able to create a well-explained protocol that can be used by all labs interested in implementing it.  

## Introduction
Long image acquisition experiments require a reliable focus stabilisation system to avoid any defocusing resulting from drift of components. In this regard, a form of focus stabilization in which the sample is maintained in focus is desirable.

## Method
The approach that we employ for this project relies upon developing microscopes that integrate not only the illumination and detection paths, but also the optical focus stabilisation path. Our focus stabilization path relies on imaging and monitoring the change in the intensity profile of the IR laser beam reflected from the glass coverslip. Any change in the distance between the objective lens and the glass coverslip results in a lateral shift in the position of the returning beam, which is detected by the camera. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. A software-based feedback system detects this shift and corrects it by adjusting the position of the piezoelectric element built into the sample stage. By altering the intensity distribution of a back-reflected beam at the camera, this method reports defocusing value and direction when the axial position of the glass coverslip or imaging objective lens changes.

## Characterisation

## Components
  * Laser [λ = 850 nm, CPS850, Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS850)
  * Relay lens pair
  * Camera
  * 50/50 Beam Splitter (λ = 300-1100 nm)
  * Dichroic (12.5x17.6 mm, 800 nm, Shortpass Dichroic Mirror,	Edmund Optics	#69-196)

## Codes
  * PiFocusASI.py: To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * PiCamAcquisition.py: To acquire a Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage. 

## References:
  1. Bon, P., Bourg, N., Lécart, S. et al. Three-dimensional nanometre localization of nanoparticles to enhance super-resolution microscopy. Nat Commun 6, 7764 (2015). [DOI: 10.1038/ncomms8764](https://doi.org/10.1038/ncomms8764)
