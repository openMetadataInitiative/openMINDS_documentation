######################
QuantitativeValueRange
######################

https://openminds.ebrains.eu/core/QuantitativeValueRange
--------------------------------------------------------

A representation of a range of quantitative values.

------------

------------

**********
Properties
**********

:Required: `maxValue <maxValue_heading_>`_, `minValue <minValue_heading_>`_
:Optional: `unit <unit_heading_>`_

------------

.. _maxValue_heading:

maxValue
--------

Greatest quantity attained or allowed.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/maxValue
   :value type: number
   :instructions: Add the maximum value measured for this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValue_heading:

minValue
--------

Smallest quantity attained or allowed.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/minValue
   :value type: number
   :instructions: Add the minimum value measured for this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _unit_heading:

unit
----

Determinate quantity adopted as a standard of measurement.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds.ebrains.eu/controlledTerms/UnitOfMeasurement>`_
   :instructions: Add the unit of measurement of this quantitative value range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

