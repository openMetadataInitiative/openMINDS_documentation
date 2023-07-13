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
:Optional:

------------

.. _maxValue_heading:

maxValue
--------

Greatest quantity attained or allowed.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/maxValue
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Add the maximum quantitative value of this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValue_heading:

minValue
--------

Smallest quantity attained or allowed.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/minValue
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Add the minimum quantitative value of this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

