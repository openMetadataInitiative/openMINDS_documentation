#################
NumericalProperty
#################

:Semantic name: https://openminds.ebrains.eu/core/NumericalProperty

:Display as: Numerical property

Structured information about a property of some entity or process whose value is a number.


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `value <value_heading_>`_
:Optional:

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this numerical property.

`BACK TO TOP <NumericalProperty_>`_

------------

.. _value_heading:

*****
value
*****

Entry for a property.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/value
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter all quantitative values that are described by this numerical property.

`BACK TO TOP <NumericalProperty_>`_

------------

