###############
CoordinatePoint
###############

https://openminds.ebrains.eu/sands/CoordinatePoint
--------------------------------------------------

Structured information on a coordinate point.

------------

------------

**********
Properties
**********

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `coordinates <coordinates_heading_>`_
:Optional:

------------

.. _coordinateSpace_heading:

coordinateSpace
---------------

Two or three dimensional geometric setting.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | `CommonCoordinateSpaceVersion <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_or `CustomCoordinateSpace
                <https://openminds.ebrains.eu/sands/CustomCoordinateSpace>`_
   :instructions: Add the coordinate space in which this coordinate point exists in.

`BACK TO TOP <CoordinatePoint_>`_

------------

.. _coordinates_heading:

coordinates
-----------

Pair or triplet of numbers defining a location in a given coordinate space.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinates
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the coordinates of this point within the stated coordinate space for two-dimensonal spaces as [x, y] or for three-dimensional space as
      [x, y, z].

`BACK TO TOP <CoordinatePoint_>`_

------------

