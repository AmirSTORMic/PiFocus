# PiFocus: A universal autofocusing approach using astigmatism

### Amir Rahmani<sup>1</sup>, Aleks Ponjavic<sup>1</sup>
#### 1: *School of Physics and Astronomy, University of Leeds, Leeds, UK*

## Abstract
<p align="justify">
In single-molecule localisation microscopy (SMLM), tens of thousands of frames of individual fluorophores are often sequentially recorded to build up a super-resolution image of a target of interest e.g., a protein in a cell. For these long-term image acquisition experiments, a reliable real-time autofocus system with precision at the nanometre scale is required to prevent defocusing. Most existing focus stabilization systems utilize a total internal reflection optical path for the autofocus beam as the high lateral motion of a reflected beam due to focal drift is significant. However, these techniques are not compatible with low numerical aperture (NA) systems because of the restricted angle of incidence. Here, we present the development of a universal autofocus system that is compatible with a broad range of objective lenses spanning from low to high NA. Our approach relies on astigmatic imaging and monitoring the change upon focal drift in the intensity profile of the IR laser beam reflected from a glass coverslip. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. We have implemented our solution on a Raspberry PI platform that is capable of performing autofocusing at 300 fps, which is suitable for most conventional SMLM and tracking applications. This also means that the solution is independent and can be turned off/on when required without affecting any fluorescence imaging process. By calibrating the astigmatic response, it is also possible to do whole-cell scanning with autofocus.  
</p>

## Introduction
<p align="justify">
Optical microscopy is basically the imaging of samples positioned at the focal plane of the primary objective lens. Maintaining optimal focus in real-time becomes crucial due to potential axial drift caused by external factors, including mechanical and thermal influences. Although extensive research, as evidenced by numerous patents and papers [1, 2], has been undertaken to develop autofocusing mechanisms, most of them suffer from either low focus correction precision or low acquisition range. Super-resolution microscopy techniques such as SMLM and MIINFLUX which obtain images of the biological samples at the nanoscale resolution feel the need for a robust and precise real-time autofocus system more importantly for high-throughput automated microscopy. Hence, in addition to autofocusing method developments [references will be added] several commercial systems have been designed [cite Perfect Focus System] to cater to the needs of microscopists in achieving accurate and consistent focus during imaging sessions. Still, 
</p>

## Methods
<p align="justify">
The collimated output beam of the IR laser was directed to pass through a beam expansion configuration which is utilized to ensure the required beam size at the back aperture of the objective lens. The collimated expanded beam then was reflected by a polarizing beam splitter (PBS) and passed through a λ/4-plate for circular polarization. The beam entered the microscopy path by being reflected from the dichroic heading towards the back aperture of the primary objective lens. The laser beam is then focused on the glass coverslip at the front focal plane of the objective lens. The reflected light from the glass coverslip took the same path back to the autofocus detection unit by transmitting through the PBS, filtered by a neutral density filter, passing through a cylindrical lens (f = 500 mm) and focused onto a camera (Raspberry Pi OV-CAM) by a tube lens (f = 200, Thorlabs Inc.) where it formed an elliptical Gaussian PSF.  
</p>

<p align="justify">
Our focus stabilization path relies on encoding the axial position of the glass coverslip by real-time monitoring of the reflected beam. The beam profile on the camera is circular when the sample is in focus and becomes an ellipse when it is out of focus and this means the beam width would vary in X and Y which informs us of the change in the axial sample position and the direction it has been displaced towards. This dependency of the beam width in XY to the axial position of the glass coverslip can help us to fit the curve and the axial calibration curve can be obtained by subtracting the beam width change for x and y.  
</p>

<p align="justify">
According to the theory of Fraunhofer diffraction for circular apertures, the intensity at the image plane would be 
</p>

## Results and Discussion
in a closed-loop feedback system and had a precision of less than ------- with a 20 µm focus range.
  * Focusing Error Curves
  * For objective lenses from low to high NA
  * Timelapse 

## Acknowledgements
<p align="justify">
The authors gratefully acknowledge the help from Robert Elliott, Tabitha Cox, Thomas Marsh, and, Akhila Thamaravelil Abhimanue Achary in the School of Physics and Astronomy at the University of Leeds who helped with setting up the Raspberry Pi, coding, and data acquisition.
</p>

## Data availability

## Funding
Engineering and Physical Sciences Research Council.

## References:
  1. G. Reinheimer, Anordnung zum selbsttätigen Fokussieren auf in optischen Geräten zu betrachtende Objekte, German Patent No. DE-PS 21 02 922 (1971).
  2. Donald K. Cohen, Wing Ho Gee, M. Ludeke, and Julian Lewkowicz, "Automatic focus control: the astigmatic lens approach," Appl. Opt. 23, 565-570 (1984) DOI: [10.1364/AO.23.000565](https://doi.org/10.1364/AO.23.000565)
  3. B. Neumann, Autofocusing (Autofokussierung), Measuring Methods Using Optoelectronic Semiconductor Components, p 135-148(SEE N 86-14556 05-35), (1985). [LINK](https://scholar.google.com/scholar_lookup?title=Autofokussierung&publication_year=1985&author=B.%20Neumann)
  4. B. Neumann and G. Reinheimer, Vorrichtung zum selbsttätigen Fokussieren auf in optischen Geräten zu betrachtende Objekte, German Patent No. DE-PS 32 19 503 (1985).
  5. Bon, P., Bourg, N., Lécart, S. et al. Three-dimensional nanometre localization of nanoparticles to enhance super-resolution microscopy. Nat Commun 6, 7764 (2015). DOI: [10.1038/ncomms8764](https://doi.org/10.1038/ncomms8764)
  6. Hongqiang Ma and Yang Liu, "Embedded nanometer position tracking based on enhanced phasor analysis," Opt. Lett. 46, 3825-3828 (2021), DOI: [10.1364/OL.433740](https://doi.org/10.1364/OL.433740)
  7. Coelho, S., Baek, J., Walsh, J. et al. 3D active stabilization for single-molecule imaging. Nat Protoc 16, 497–515 (2021). DOI: [10.1038/s41596-020-00426-9](https://doi.org/10.1038/s41596-020-00426-9)
  8. Rajdeep Chowdhury, Abhishek Sau, Jerry Chao, Ankith Sharma, and Siegfried M. Musser, "Tuning axial and lateral localization precision in 3D super-resolution microscopy with variable astigmatism," Opt. Lett. 47, 5727-5730 (2022) DOI: [10.1364/OL.466213](https://doi.org/10.1364/OL.466213)