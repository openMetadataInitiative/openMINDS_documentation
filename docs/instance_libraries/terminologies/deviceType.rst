#################################
Terminologies: DeviceType library
#################################

Related schema specification: `DeviceType <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/deviceType.html>`_

------------

------------

CTscanner
---------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/CTscanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'CT scanner' is an x-ray machine that creates and combines serial two-dimensional x-ray images (sections) with the aid of a computer to generate cross-sectional views and/or three-dimensional images of internal body structures (e.g., bones, blood vessels or soft tissues).
   :name: CT scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIBodyCoil
-----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIBodyCoil
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of volume coil optimized for uniform radiofrequency transmission and/or reception across large anatomical regions, typically encompassing the torso or entire body.
   :description: Body coils are integrated volume coils typically built into the bore of an MRI scanner to provide homogeneous B1 field distribution across extensive anatomical areas. They are often used as transmit or transmit/receive coils for imaging the torso and whole body, and frequently serve as the system's default transmit coil when combined with local receive arrays. Their large geometry ensures consistent excitation and reception, enabling high-quality imaging across diverse body regions and supporting calibration or reference functions in multi-coil setups.
   :name: MRI body coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIExtremityCoil
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIExtremityCoil
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of volume coil optimized for imaging peripheral anatomical regions such as the arms, legs, wrists, ankles, or knees; in rare cases, extremity coils may adopt a surface-coil design when full enclosure of the anatomy is impractical.
   :description: Extremity coils are specialized radiofrequency volume coils designed to provide high signal-to-noise ratio and uniform excitation when imaging smaller body parts like the limbs. They typically use cylindrical or contoured geometries that enclose the target region but can also appear as surface-coil variants for joints or areas where full coverage is not feasible. Extremity coils are widely used in musculoskeletal and vascular MRI, offering focused, high-resolution imaging of localized peripheral structures.
   :name: MRI extremity coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIHeadCoil
-----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIHeadCoil
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of volume coil optimized for radiofrequency transmission and/or reception over the head and brain, providing homogeneous B1 field coverage within the cranial region.
   :description: Head coils are dedicated radiofrequency (RF) volume coils designed to image the brain and cranial structures. They typically use birdcage or quadrature configurations to achieve uniform excitation and reception across the entire head. Head coils can operate as transmit/receive or receive-only systems depending on the scanner design. High-channel phased-array head coils are increasingly common, improving signal-to-noise ratio (SNR) and parallel-imaging capabilities. In some advanced configurations, open or partial head coils are employed for interventional or functional MRI studies, where full enclosure is not required.
   :name: MRI head coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIMulti-coilArray
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIMulti-coilArray
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of radiofrequency coil composed of multiple coordinated elements optimized for transmit and/or receive operation over an extended field of view; phased-array coils are a specialized subclass focused on parallel signal reception.
   :description: Multi-coil arrays consist of several individual RF elements that work together to improve signal quality, coverage, and control of the B₁ field. Depending on their configuration, they may operate as transmit, receive, or transmit-receive systems, enabling techniques such as RF shimming, parallel transmission, and parallel imaging. These arrays can be designed with volume-type geometries that enclose the anatomy or surface-type arrangements that conform to the body's contour. Phased-array coils represent a subset of multi-coil arrays specialized for independent receive channels used in parallel acquisition.
   :name: MRI multi-coil array

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRISurfaceCoil
--------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRISurfaceCoil
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of radiofrequency coil optimized for localized signal reception from tissue near the coil surface, providing high sensitivity over a small field of view.
   :description: Surface coils are small radiofrequency coils placed directly adjacent to the region of interest to capture strong signals from nearby tissues with high spatial resolution. Their sensitivity decreases rapidly with distance, making them ideal for imaging superficial structures such as the spine, joints, or breast. Surface coils are typically receive-only and operate in combination with a separate transmit coil, often the body coil. They can also serve as building blocks in multi-coil or phased-array configurations, extending coverage while maintaining local sensitivity.
   :name: MRI surface coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIVolumeCoil
-------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIVolumeCoil
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: Type of radiofrequency coil optimized for uniform transmit and/or receive coverage across a defined enclosed volume of anatomy.
   :description: Volume coils are radiofrequency coils that fully or partially enclose the anatomy to produce a homogeneous B₁ field within a specified region, such as the head, torso, or extremities. They are used for both transmission and reception of MR signals and are commonly built in birdcage or quadrature configurations. Volume coils provide uniform excitation and reception, making them suitable for general-purpose imaging or as transmit coils in combination with local receive arrays. Their subtypes include body, head, and extremity coils, which differ mainly by size and anatomical coverage.
   :name: MRI volume coil

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

MRIscanner
----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/MRIscanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: An 'MRI scanner' is a machine that uses strong magnetic fields, magnetic field gradients, and radio waves to generate static or time-resolved three-dimensional images of the anatomy and physiological processes of the body.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106463
   :name: MRI scanner
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/birnlex_2100

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

closedBoreMRIScanner
--------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/closedBoreMRIScanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: 'Closed-bore MRI scanners' are high-field scanners which feature a magnet surrounding the patient creating a capsule-like space (standard or wide) where the patient lies on.
   :name: closed-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

electronicAmplifier
-------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/electronicAmplifier
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: An 'electronic amplifier' is a device that increases the power (voltage or current) of a time-varying signal.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0100567
   :name: electronic amplifier
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/nlx_27076

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

microscope
----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/microscope
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'microscope' is an instrument used to obtain a magnified image of small objects and reveal details of structures not otherwise distinguishable.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106921
   :name: microscope
   :preferredOntologyIdentifier: http://uri.neuinfo.org/nif/nifstd/birnlex_2106

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

microtome
---------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/microtome
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'microtome' is a mechanical instrument with a steel, glass or diamond blade used to cut (typically) biological specimens into very thin segments for further treatment and ultimately microscopic or histologic examination.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0106925
   :name: microtome
   :preferredOntologyIdentifier: http://purl.obolibrary.org/obo/OBI_0400168

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

openBoreMRIScanner
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/openBoreMRIScanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: 'Open-bore MRI scanners' are low-field scanners which have a magnetic top and bottom, but are otherwise open, increasing patient's comfort and unobstructed view of the scanning area.
   :name: open-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

standardBoreMRIScanner
----------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/standardBoreMRIScanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'standard-bore MRI scanner' is a closed high-field scanner which features a magnet surrounding the patient creating a capsule-like space where the patient lies on.
   :name: standard-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

vibratingMicrotome
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/vibratingMicrotome
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'vibrating microtome' is an mechanical instrument with a vibrating steel blade used to cut (typically) biological specimens into thin segments for further treatment and ultimately microscopic or histologic examination.
   :interlexIdentifier: http://uri.interlex.org/base/ilx_0780522
   :name: vibrating microtome

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

wideBoreMRIScanner
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.ebrains.eu/vocab/>
   :@id: https://openminds.ebrains.eu/instances/deviceType/wideBoreMRIScanner
   :@type: https://openminds.ebrains.eu/controlledTerms/DeviceType
   :definition: A 'wide-bore MRI scanner' is a closed high-field scanner which features a widened bore compared to the standard-bore MRI scanner.
   :name: wide-bore MRI scanner

`BACK TO TOP <Terminologies: DeviceType library_>`_

------------

