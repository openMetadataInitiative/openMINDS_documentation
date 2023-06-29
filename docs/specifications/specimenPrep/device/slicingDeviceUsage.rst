##################
SlicingDeviceUsage
##################

https://openminds.ebrains.eu/specimenPrep/SlicingDeviceUsage
------------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `device <device_heading_>`_, `sliceThickness <sliceThickness_heading_>`_, `slicingPlane <slicingPlane_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `oscillationAmplitude <oscillationAmplitude_heading_>`_,
   `slicingAngle <slicingAngle_heading_>`_, `slicingSpeed <slicingSpeed_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_, `vibrationFrequency
   <vibrationFrequency_heading_>`_

------------

.. _device_heading:

device
------

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `SlicingDevice <https://openminds.ebrains.eu/specimenPrep/SlicingDevice>`_
   :instructions: Add the slicing device used.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _metadataLocation_heading:

metadataLocation
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_ or `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _oscillationAmplitude_heading:

oscillationAmplitude
--------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/oscillationAmplitude
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the oscillation amplitude of the blade from the slicing device during its use.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _sliceThickness_heading:

sliceThickness
--------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/sliceThickness
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the defined slice thickness during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingAngle_heading:

slicingAngle
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/slicingAngle
   :value type: | embedded object array \(1-2\) of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `NumericalProperty
                <https://openminds.ebrains.eu/core/NumericalProperty>`_
   :instructions: Enter all slicing angles (intentional or unintentional) in relation to the slicing plane used during this activity.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingPlane_heading:

slicingPlane
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/slicingPlane
   :value type: | linked object of type
                | `AnatomicalPlane <https://openminds.ebrains.eu/controlledTerms/AnatomicalPlane>`_
   :instructions: Add the anatomical plane that best describes the slicing direction of the tissue sample(s) during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _slicingSpeed_heading:

slicingSpeed
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/slicingSpeed
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the defined slicing speed during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _usedSpecimen_heading:

usedSpecimen
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_ or `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

.. _vibrationFrequency_heading:

vibrationFrequency
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/vibrationFrequency
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the defined vibration frequency during the use of this slicing device.

`BACK TO TOP <SlicingDeviceUsage_>`_

------------

