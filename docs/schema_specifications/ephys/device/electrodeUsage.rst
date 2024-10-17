##############
ElectrodeUsage
##############

:Semantic name: ephys:ElectrodeUsage

:Display as: Ephys:electrode usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `contactResistance <contactResistance_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `spatialLocation <spatialLocation_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the electrode contact.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _contactResistance_heading:

*****************
contactResistance
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactResistance
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the contact resistance of this electrode during its use.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | ephys:Electrode \[TYPE_ERROR\]
   :instructions: Add the electrode used.

`BACK TO TOP <ElectrodeUsage_>`_

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

`BACK TO TOP <ElectrodeUsage_>`_

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

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point that best describes the spatial location of the electrode contact during its use.

`BACK TO TOP <ElectrodeUsage_>`_

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

`BACK TO TOP <ElectrodeUsage_>`_

------------

