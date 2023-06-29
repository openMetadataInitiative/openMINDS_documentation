#################
PropertyValueList
#################

***************************************************
https://openminds.ebrains.eu/core/PropertyValueList
***************************************************

An identifiable list of property-value pairs.

------------

------------

**********
Properties
**********

:Required: `propertyValuePair <propertyValuePair_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this property-value list that may help you to find this instance more easily.

`BACK TO TOP <PropertyValueList_>`_

------------

.. _propertyValuePair_heading:

propertyValuePair
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/propertyValuePair
   :value type: | embedded object array \(1-N\) of type
                | `NumericalProperty <https://openminds.ebrains.eu/core/NumericalProperty>`_or `StringProperty
                <https://openminds.ebrains.eu/core/StringProperty>`_
   :instructions: Enter all numerical and string property-value pairs that belong to this property-value list.

`BACK TO TOP <PropertyValueList_>`_

------------

