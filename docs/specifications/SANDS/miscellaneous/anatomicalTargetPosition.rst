########################
AnatomicalTargetPosition
########################

https://openminds.ebrains.eu/sands/AnatomicalTargetPosition
-----------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `anatomicalTarget <anatomicalTarget_heading_>`_, `targetIdentificationType <targetIdentificationType_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `spatialLocation <spatialLocation_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concering this anatomical target position.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _anatomicalTarget_heading:

anatomicalTarget
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalTarget
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `SubcellularEntity
                <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_ or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all anatomical entities that describe the target position(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _spatialLocation_heading:

spatialLocation
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object array \(1-N\) of type
                | `CoordinatePoint <https://openminds.ebrains.eu/sands/CoordinatePoint>`_
   :instructions: Add all coordinate points that describe the spatial location of the anatomical target structure(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _targetIdentificationType_heading:

targetIdentificationType
------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/targetIdentificationType
   :value type: | linked object of type
                | `AnatomicalIdentificationType <https://openminds.ebrains.eu/controlledTerms/AnatomicalIdentificationType>`_
   :instructions: Add the target identification type that best describes how the this anatomical target position was identified.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

