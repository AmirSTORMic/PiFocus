# πFocus: A universal autofocusing approach using astigmatism

### Amir Rahmani<sup>1</sup>, Aleks Ponjavic<sup>1</sup>
#### 1: *School of Physics and Astronomy, University of Leeds, Leeds, UK*

## Abstract
In single-molecule localisation microscopy (SMLM), tens of thousands of frames of individual fluorophores are often sequentially recorded to build up a super-resolution image of a target of interest e.g., a protein in a cell. For these long-term image acquisition experiments, a reliable real-time autofocus system with precision at the nanometre scale is required to prevent defocusing. Most existing focus stabilization systems utilize a total internal reflection optical path for the autofocus beam as the high lateral motion of a reflected beam due to focal drift is significant. However, these techniques are not compatible with low NA systems because of the restricted angle of incidence. Here, we present the development of a universal autofocus system that is compatible with a broad range of objective lenses spanning from low to high numerical aperture (NA). Our approach relies on astigmatic imaging and monitoring the change upon focal drift in the intensity profile of the IR laser beam reflected from a glass coverslip. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. We have implemented our solution on a Raspberry PI platform that is capable of performing autofocusing at 300 fps, which is suitable for most conventional SMLM and tracking applications. This also means that the solution is independent and can be turned off/on when required without affecting any fluorescence imaging process. By calibrating the astigmatic response, it is also possible to do whole-cell scanning with autofocus.  

## Method
The approach that we employ for this project relies upon developing microscopes that integrate not only the illumination and detection paths but also the optical focus stabilisation path. Our focus stabilization path relies on imaging and monitoring the change in the intensity profile of the IR laser beam reflected from the glass coverslip. Any change in the distance between the objective lens and the glass coverslip results in a lateral shift in the position of the returning beam, which is detected by the camera. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. A software-based feedback system detects this shift and corrects it by adjusting the position of the piezoelectric element built into the sample stage. By altering the intensity distribution of a back-reflected beam at the camera, this method reports defocusing value and direction when the axial position of the glass coverslip or imaging objective lens changes.

## Characterisation
  * Focusing Error Curves
  * For objective lenses from low to high NA
  * Timelapse 

## Main Parts
  * [Laser (λ = 850 nm, CPS850, Thorlabs)](https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS850)
  * Relay lens pair
  * Camera
  * 50/50 Beam Splitter (λ = 300-1100 nm)
  * Dichroic Mirror (12.5x17.6 mm, 800 nm, Shortpass Dichroic Mirror,	Edmund Optics	#69-196)

## Acknowledgements
The authors gratefully acknowledge the help from Robert Elliott, Tabitha Cox, Thomas Marsh, and, Akhila Thamaravelil Abhimanue Achary in the School of Physics and Astronomy at the University of Leeds who helped with setting up the Raspberry Pi, coding, and data acquisition.

## Data availability
Python scripts that have been used for hardware control, data acquisition, and analysis are available in this GitHub repository. The experimental data will be added soon. 
  * PiFocusASI.py: To acquire a Z scan data for the focus stabilisation path using the ASI camera and the CoreMorrow piezo stage. 
  * PiCamAcquisition.py: To acquire Z scan data for the focus stabilisation path using the OV camera and the CoreMorrow piezo stage.
  * [GCurFit.py](https://github.com/AmirSTORMic/PiFocus/master/GCurFit.py): To analyse the acquired datasets on the Autofocus system in the advanced lab. 
## Funding
Engineering and Physical Sciences Research Council.

## References:
  1. Bon, P., Bourg, N., Lécart, S. et al. Three-dimensional nanometre localization of nanoparticles to enhance super-resolution microscopy. Nat Commun 6, 7764 (2015). DOI: [10.1038/ncomms8764](https://doi.org/10.1038/ncomms8764)
  2. Rajdeep Chowdhury, Abhishek Sau, Jerry Chao, Ankith Sharma, and Siegfried M. Musser, "Tuning axial and lateral localization precision in 3D super-resolution microscopy with variable astigmatism," Opt. Lett. 47, 5727-5730 (2022) DOI: [10.1364/OL.466213](https://doi.org/10.1364/OL.466213)
  3. Hongqiang Ma and Yang Liu, "Embedded nanometer position tracking based on enhanced phasor analysis," Opt. Lett. 46, 3825-3828 (2021), DOI: [10.1364/OL.433740](https://doi.org/10.1364/OL.433740)
  4. Coelho, S., Baek, J., Walsh, J. et al. 3D active stabilization for single-molecule imaging. Nat Protoc 16, 497–515 (2021). DOI: [10.1038/s41596-020-00426-9](https://doi.org/10.1038/s41596-020-00426-9)
