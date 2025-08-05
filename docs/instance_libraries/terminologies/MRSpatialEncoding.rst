########################################
Terminologies: MRSpatialEncoding library
########################################

Related schema specification: `MRSpatialEncoding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRSpatialEncoding.html>`_

------------

------------

frequencyEncoding
-----------------

.. admonition:: metadata sheet

   :@id: https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyEncoding
   :@type: https://openminds.om-i.org/types/MRSpatialEncoding
   :definition: Gradients establish a direct relationship between frequency and spatial position, a process referred to as frequency encoding.
   :description: In MRI, gradients generate a controlled variation in the magnetic field strength across the imaging volume. Each location along the gradient direction corresponds to a unique frequency in the received MR signal. This process, known as frequency encoding, allows spatial information to be extracted from the signal during image reconstruction. Primarily used in specialized applications like spectroscopy.
   :name: 1D MR acquisition

`BACK TO TOP <Terminologies: MRSpatialEncoding library_>`_

------------

frequencyPhaseEncoding
----------------------

.. admonition:: metadata sheet

   :@id: https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyPhaseEncoding
   :@type: https://openminds.om-i.org/types/MRSpatialEncoding
   :definition: Using frequency encoding and phase encoding in conjunction together to acquire 2D magnetic resonance images.
   :description: In 2D frequency x phase MRI imaging, spatial localization is achieved through a combination of slice selection, frequency encoding, and phase encoding. Slice selection involves applying a gradient along one axis (typically the z-axis) during RF excitation, ensuring that only a specific tissue slice resonates based on its unique Larmor frequency. Once the slice is excited, frequency encoding is applied along another axis (usually the x-axis) during signal acquisition, creating a direct relationship between spatial position and resonance frequency. To encode the second spatial dimension (typically the y-axis), phase encoding is applied before signal acquisition, briefly altering the phase of spins based on their position. This phase shift remains embedded in the signal and is later decoded during image reconstruction, allowing for the creation of detailed 2D MR images.
   :name: Frequency x phase encoding

`BACK TO TOP <Terminologies: MRSpatialEncoding library_>`_

------------

frequencyPhasePhaseEncoding
---------------------------

.. admonition:: metadata sheet

   :@id: https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyPhasePhaseEncoding
   :@type: https://openminds.om-i.org/types/MRSpatialEncoding
   :definition: 3D MRI imaging is a technique that acquires volumetric data by using frequency encoding and two phase encoding steps, eliminating the need for slice selection and enabling high-resolution, multi-plane image reconstruction.
   :description: In 3D frequency x phase x phase MRI imaging, spatial localization is achieved using frequency encoding, phase encoding, and a second phase encoding step instead of slice selection. Unlike 2D imaging, where individual slices are excited separately, 3D MRI excites the entire imaging volume at once. Frequency encoding is applied along one axis (typically the x-axis), while phase encoding is applied along the second (usually the y-axis). To resolve the third dimension, an additional phase encoding step is applied along the slice-select direction (typically the z-axis), replacing traditional slice selection. This results in a fully sampled 3D dataset, which can be reconstructed into thin slices or reformatted in multiple planes, providing higher signal-to-noise ratio (SNR) and improved spatial resolution compared to 2D imaging.
   :name: Frequency x phase x phase encoding

`BACK TO TOP <Terminologies: MRSpatialEncoding library_>`_

------------

phaseEncoding
-------------

.. admonition:: metadata sheet

   :@id: https://openminds.om-i.org/instances/MRSpatialEncoding/phaseEncoding
   :@type: https://openminds.om-i.org/types/MRSpatialEncoding
   :definition: Gradients establish a direct relationship between phase and spatial position, a process referred to as phase encoding.
   :name: Phase encoding

`BACK TO TOP <Terminologies: MRSpatialEncoding library_>`_

------------

