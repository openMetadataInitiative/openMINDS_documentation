###############
CoordinatePoint
###############

:Semantic name: sands:CoordinatePoint

:Display as: Sands:coordinate point


------------

------------

Properties
##########

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `coordinates <coordinates_heading_>`_
:Optional:

------------

.. _coordinateSpace_heading:

***************
coordinateSpace
***************

Two or three dimensional geometric setting.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\] or sands:CustomCoordinateSpace \[TYPE_ERROR\]
   :instructions: Add the coordinate space in which this coordinate point exists in.

`BACK TO TOP <CoordinatePoint_>`_

------------

.. _coordinates_heading:

***********
coordinates
***********

Pair or triplet of numbers defining a location in a given coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinates
   :value type: | embedded object array \(2-3\) of type
                | core:QuantitativeValue \[TYPE_ERROR\]
   :instructions: Enter the coordinates of this point within the stated coordinate space for two-dimensonal spaces as [x, y] or for three-dimensional space as [x, y, z].

`BACK TO TOP <CoordinatePoint_>`_

------------

