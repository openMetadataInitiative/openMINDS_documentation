###################
ElectrodeArrayUsage
###################

:Semantic name: ephys:ElectrodeArrayUsage

:Display as: Ephys:electrode array usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_
:Optional: `anatomicalLocationOfArray <anatomicalLocationOfArray_heading_>`_, `anatomicalLocationOfElectrodes <anatomicalLocationOfElectrodes_heading_>`_, `contactResistances <contactResistances_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `spatialLocationOfElectrodes <spatialLocationOfElectrodes_heading_>`_, `usedElectrode <usedElectrode_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocationOfArray_heading:

*************************
anatomicalLocationOfArray
*************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocationOfArray
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all anatomical entities that semantically best describe the overall anatomical location of the electrode array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _anatomicalLocationOfElectrodes_heading:

******************************
anatomicalLocationOfElectrodes
******************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocationOfElectrodes
   :value type: | linked object array \(2-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all anatomical entities that semantically best describe the anatomical location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _contactResistances_heading:

******************
contactResistances
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactResistances
   :value type: | embedded object array \(2-N\) of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the contact resistance for each electrode of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | ephys:ElectrodeArray \[TYPE_ERROR\]
   :instructions: Add the electrode array used.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | core:File \[TYPE_ERROR\] or core:FileBundle \[TYPE_ERROR\]
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _spatialLocationOfElectrodes_heading:

***************************
spatialLocationOfElectrodes
***************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocationOfElectrodes
   :value type: | embedded object array \(2-N\) of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add all coordinate points that best describe the spatial location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _usedElectrode_heading:

*************
usedElectrode
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedElectrode
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the identifiers of all electrodes that are actually in use for this array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | core:SubjectState \[TYPE_ERROR\] or core:TissueSampleState \[TYPE_ERROR\]
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

