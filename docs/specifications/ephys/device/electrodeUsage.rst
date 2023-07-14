##############
ElectrodeUsage
##############

:Semantic name: https://openminds.ebrains.eu/ephys/ElectrodeUsage


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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the electrode contact.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _contactResistance_heading:

*****************
contactResistance
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the contact resistance of this electrode during its use.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `Electrode <https://openminds-documentation.readthedocs.io/en/latest/specifications/ephys/device/electrode.html>`_
   :instructions: Add the electrode used.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: specifications

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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point that best describes the spatial location of the electrode contact during its use.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <ElectrodeUsage_>`_

------------

