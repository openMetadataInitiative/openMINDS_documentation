###################
ViewerSpecification
###################

:Semantic name: https://openminds.ebrains.eu/sands/ViewerSpecification


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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concerning this viewer specification.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _anchorPoint_heading:

***********
anchorPoint
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anchorPoint
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the coordinates of the anchor point that a viewer should use. Either state the anchor point of the annotation again or state another coordinate point.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _cameraPosition_heading:

**************
cameraPosition
**************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/cameraPosition
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Enter the camera position that a viewer should use.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _preferredDisplayColor_heading:

*********************
preferredDisplayColor
*********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preferredDisplayColor
   :value type: | linked object of type
                | `Colormap <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/colormap.html>`_ or `SingleColor <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/miscellaneous/singleColor.html>`_
   :instructions: Add the preferred color that a viewer should display.

`BACK TO TOP <ViewerSpecification_>`_

------------

