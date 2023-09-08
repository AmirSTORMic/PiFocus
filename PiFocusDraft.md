# A universal focus stabilization approach using astigmatism: from low to high NA

### Amir Rahmani<sup>1</sup>, Aleks Ponjavic<sup>1</sup>
#### 1: *School of Physics and Astronomy, University of Leeds, Leeds, UK*

## Abstract
<p align="justify">
In single-molecule localization microscopy (SMLM), tens of thousands of frames of individual fluorophores are often sequentially recorded to build up a super-resolution image of a target of interest e.g., a protein in a cell. For these long-term image acquisition experiments, a reliable real-time autofocus system with precision at the nanometre scale is required to prevent defocusing. Most existing focus stabilization systems utilize a total internal reflection optical path for the autofocus beam as the high lateral motion of a reflected beam due to focal drift is significant. However, these techniques are not compatible with low numerical aperture (NA) systems because of the restricted angle of incidence. Here, we present the development of a universal autofocus system that is compatible with a broad range of objective lenses spanning from low to high NA. Our approach relies on astigmatic imaging and monitoring the change upon focal drift in the intensity profile of the IR laser beam reflected from a glass coverslip. The system allows for controlling hardware components and performs sample focus stabilization to counter sample drift in the Z-axis using a closed-loop feedback signal between the IR beam profile position and the piezo stage. We have implemented our solution on a Raspberry PI platform that is capable of performing autofocusing at 300 fps, which is suitable for most SMLM methods, MINFLUX, and tracking applications. This also means that the solution is independent and can be turned off/on when required without affecting any fluorescence imaging process. By calibrating the astigmatic response, it is also possible to do whole-cell scanning with autofocus.  
</p>

## Introduction
<p align="justify">
Optical microscopy is basically the imaging of samples positioned at the focal plane of the primary objective lens. Maintaining optimal focus in real-time becomes crucial due to potential axial drift caused by external factors, including mechanical and thermal influences. Although extensive research, as evidenced by numerous patents and papers [1, 2], has been undertaken to develop focus stabilization mechanisms, most of them suffer from either low defocus correction precision or low working range. Super-resolution microscopy techniques which obtain images of the biological samples at the nanoscale resolution feel the need for a robust and precise real-time focus stabilization system more importantly for high-throughput automated microscopy. More importantly, for applications in single-molecule tracking which in lateral drift doesn't interrupt the experiments as it is much less in a short timescale compared to the molecule of interest movement. Hence, in addition to the focus stabilization method developments, several commercial systems have been designed [Perfect Focus and Definite Focus systems] to cater to the needs of microscopists in achieving accurate and consistent focus during imaging sessions. The ability to seamlessly switch between primary objective lenses of varying magnifications and numerical apertures is important to speed up the experiments on many biological samples. To enable such versatility, we dedicated substantial effort to the development of an axial focus stabilization approach that can be useful for single-molecule tracking and super-resolution microscopy applications. Our primary objective was to achieve a harmonious balance between adaptability and precision, thereby empowering comprehensive and insightful explorations of intricate biological samples.
</p>

## Methods
<p align="justify">
Our focus stabilization approach relies on encoding the axial position of the sample by inducing astigmatism to the back-reflected beam and real-time monitoring of its shape. The beam profile on the camera is circular when the sample is in focus and becomes an ellipse when it is out of focus and this means the beam width would vary in X and Y which informs us of the change in the axial sample position and the direction it has been displaced towards. This dependency of the beam width in XY to the axial position of the glass coverslip can help us detect any nanoscale axial drift of the glass coverslip and correct it with the piezo sample stage. 
</p>

<p align="justify">
The collimated output beam of the near IR laser was directed to pass through a beam expansion configuration which is utilized to ensure the required beam size at the back aperture of the objective lens. The collimated expanded beam then was reflected by a polarizing beam splitter (PBS) and passed through a λ/4-plate for circular polarization. The beam entered the microscopy path by being reflected from the dichroic heading towards the back aperture of the primary objective lens (O1). The laser beam is then focused on the glass coverslip at the front focal plane of the O1. The back-reflected light from the interface of the immersion medium and the glass coverslip took the same path back to the focus stabilization detection optical path by transmitting through the PBS, filtered by a neutral density filter, passing through a cylindrical lens (f = 500/1000 mm), and focused onto a camera (Raspberry Pi OV-CAM/ZWO ASI) by a tube lens (f = 200, Thorlabs Inc.) where it formed an astigmatic shape. The back reflected beam in the optical detection pathway of the focus stabilization nit is orthogonally polarized with respect to the illumination beam and thus transmitted by the PBS. This stabilization unit was implemented as an add-on to one of our custom-built microscopes. The sample on this microscope is mounted on an XYZ piezo stage that allows fast and precise sample positioning in three dimensions. 
</p>
<!---
<p align="justify">
According to the theory of Fraunhofer diffraction for circular apertures, the intensity at the image plane would be 
</p>
-->
<p align="justify">
To perform the calibration step which is critical in ensuring the accuracy and reliability of our focus stabilization systems (especially when accounting for different optical parameters such as objective lenses' numerical aperture and astigmatism values), a Z image stack was captured to establish a calibration curve that maps the relationship between focal plane position and the corresponding correction needed for optimal focus stabilization. The scan range and step size of the Z stack were carefully chosen to ensure that the entire range of astigmatism was covered, thereby encompassing the full range of potential focal plane deviations. A three-axis piezoelectric stage (SLC-1780-D-S, SmarAct) equipped with an integrated position sensor to perform closed-loop movements, was used to control the position of the sample on the microscope stage in three dimensions.
</p>

<p align="justify">
The data acquisition and instrument control was performed with MicroManager2.0. Data analysis and processing were performed with scripts written in Python. 
</p>

## Results and Discussion
Presented in SMLMS2023 in Vienna! Coming soon!

### Nanometre localization precision of the astigmatic beam profile
<p align="justify">
It's essential to highlight that by imaging the reflected laser beam onto the camera, we benefit from an abundant supply of photons, resulting in improved localization precision. Nonetheless, this precision remains subject to limitations imposed by factors such as laser fluctuations, background noise, and camera noise. The speed at which these measurements can be performed also plays a crucial role, as there is a trade-off between localization speed and precision. The choice of the algorithm should be guided by finding the optimal balance between these two factors. The axial calibration curve was obtained by subtracting the beam width change for x and y. In each frame, the beam profile was fitted to a 2D Gaussian to locate the centre position of the beam on the Raspberry Pi camera.
 </p>
 
### Comparison with other focus stabilization approaches
<p align="justify">
To compare the performance of PiFocus with other state-of-the-art focus stabilization techniques, we activated the Perfect Focus system on the same microscope to measure the axial defocus correction precision. The Perfect Focus System operates by employing a near-infrared LED positioned off-axis to illuminate the sample space in a triangulation geometry. The reflected beam from the coverslip is then directed back through the offset lens, which focuses it onto the CCD line sensor.  It is important to note that the accuracy level provided by PFS is around 20 nm, which means that it may not be able to detect minor axial drift in the range of a few nanometers. In such cases, there might be limitations in reliably correcting for axial defocus.
</p>

## Discussion
- Since we employ a light source with a near IR wavelength, we avoid interfering with the fluorescence emissions of diverse fluorescent samples.
- Axial drift correction with a few nanometers of precision
- Field-dependent aberrations don't have any effects on our approach

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
