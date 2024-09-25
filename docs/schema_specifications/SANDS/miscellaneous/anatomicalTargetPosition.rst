########################
AnatomicalTargetPosition
########################

:Semantic name: sands:AnatomicalTargetPosition

:Display as: Sands:anatomical target position


------------

------------

Properties
##########

:Required: `anatomicalTarget <anatomicalTarget_heading_>`_, `targetIdentificationType <targetIdentificationType_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `spatialLocation <spatialLocation_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this anatomical target position.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _anatomicalTarget_heading:

****************
anatomicalTarget
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalTarget
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all anatomical entities that describe the target position(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object array \(1-N\) of type
                | sands:CoordinatePoint \[TYPE_ERROR\]
   :instructions: Add all coordinate points that describe the spatial location of the anatomical target structure(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _targetIdentificationType_heading:

************************
targetIdentificationType
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/targetIdentificationType
   :value type: | linked object of type
                | controlledTerms:AnatomicalIdentificationType \[TYPE_ERROR\]
   :instructions: Add the target identification type that best describes how the this anatomical target position was identified.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

