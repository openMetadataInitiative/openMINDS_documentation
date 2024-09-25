###################
ViewerSpecification
###################

:Semantic name: sands:ViewerSpecification

:Display as: Sands:viewer specification


------------

------------

Properties
##########

:Required: `anchorPoint <anchorPoint_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `cameraPosition <cameraPosition_heading_>`_, `preferredDisplayColor <preferredDisplayColor_heading_>`_

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
   :instructions: Enter any additional remarks concerning this viewer specification.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _anchorPoint_heading:

***********
anchorPoint
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anchorPoint
   :value type: | embedded object array \(2-3\) of type
                | core:QuantitativeValue \[TYPE_ERROR\]
   :instructions: Enter the coordinates of the anchor point that a viewer should use. Either state the anchor point of the annotation again or state another coordinate point.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _cameraPosition_heading:

**************
cameraPosition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/cameraPosition
   :value type: | embedded object of type
                | sands:CoordinatePoint \[TYPE_ERROR\]
   :instructions: Enter the camera position that a viewer should use.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _preferredDisplayColor_heading:

*********************
preferredDisplayColor
*********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preferredDisplayColor
   :value type: | linked object of type
                | controlledTerms:Colormap \[TYPE_ERROR\] or sands:SingleColor \[TYPE_ERROR\]
   :instructions: Add the preferred color that a viewer should display.

`BACK TO TOP <ViewerSpecification_>`_

------------

