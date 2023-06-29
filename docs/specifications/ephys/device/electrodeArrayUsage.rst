###################
ElectrodeArrayUsage
###################

https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage
------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `device <device_heading_>`_
:Optional: `anatomicalLocationOfArray <anatomicalLocationOfArray_heading_>`_, `anatomicalLocationOfElectrodes <anatomicalLocationOfElectrodes_heading_>`_,
   `contactResistances <contactResistances_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_,
   `spatialLocationOfElectrodes <spatialLocationOfElectrodes_heading_>`_, `usedElectrode <usedElectrode_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocationOfArray_heading:

anatomicalLocationOfArray
-------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocationOfArray
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `SubcellularEntity
                <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all anatomical entities that semantically best describe the overall anatomical location of the electrode array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _anatomicalLocationOfElectrodes_heading:

anatomicalLocationOfElectrodes
------------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocationOfElectrodes
   :value type: | linked object array \(2-N\) of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `SubcellularEntity
                <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all anatomical entities that semantically best describe the anatomical location of each electrode contact of this array during its use, in
      the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _contactResistances_heading:

contactResistances
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactResistances
   :value type: | embedded object array \(2-N\) of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the contact resistance for each electrode of this array during its use, in the same order that the electrode identifiers for this
      electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _device_heading:

device
------

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `ElectrodeArray <https://openminds.ebrains.eu/ephys/ElectrodeArray>`_
   :instructions: Add the electrode array used.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _metadataLocation_heading:

metadataLocation
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_or `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _spatialLocationOfElectrodes_heading:

spatialLocationOfElectrodes
---------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocationOfElectrodes
   :value type: | embedded object array \(2-N\) of type
                | `CoordinatePoint <https://openminds.ebrains.eu/sands/CoordinatePoint>`_
   :instructions: Add all coordinate points that best describe the spatial location of each electrode contact of this array during its use, in the same order
      that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _usedElectrode_heading:

usedElectrode
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedElectrode
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the identifiers of all electrodes that are actually in use for this array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _usedSpecimen_heading:

usedSpecimen
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_or `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

