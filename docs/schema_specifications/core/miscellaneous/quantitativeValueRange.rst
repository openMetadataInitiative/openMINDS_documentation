######################
QuantitativeValueRange
######################

:Semantic name: core:QuantitativeValueRange

:Display as: Core:quantitative value range


------------

------------

Properties
##########

:Required: `maxValue <maxValue_heading_>`_, `minValue <minValue_heading_>`_
:Optional: `maxValueUnit <maxValueUnit_heading_>`_, `minValueUnit <minValueUnit_heading_>`_

------------

.. _maxValue_heading:

********
maxValue
********

Greatest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/maxValue
   :value type: number
   :instructions: Enter the maximum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _maxValueUnit_heading:

************
maxValueUnit
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/maxValueUnit
   :value type: | linked object of type
                | controlledTerms:UnitOfMeasurement \[TYPE_ERROR\]
   :instructions: Add the unit of measurement for the maximum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValue_heading:

********
minValue
********

Smallest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/minValue
   :value type: number
   :instructions: Enter the minimum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValueUnit_heading:

************
minValueUnit
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/minValueUnit
   :value type: | linked object of type
                | controlledTerms:UnitOfMeasurement \[TYPE_ERROR\]
   :instructions: Add the unit of measurement for the minimum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

