#################
PropertyValueList
#################

:Semantic name: core:PropertyValueList

:Display as: Core:property value list


------------

------------

Properties
##########

:Required: `propertyValuePair <propertyValuePair_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this property-value list that may help you to find this instance more easily.

`BACK TO TOP <PropertyValueList_>`_

------------

.. _propertyValuePair_heading:

*****************
propertyValuePair
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/propertyValuePair
   :value type: | embedded object array \(1-N\) of type
                | core:NumericalProperty \[TYPE_ERROR\] or core:StringProperty \[TYPE_ERROR\]
   :instructions: Enter all numerical and string property-value pairs that belong to this property-value list.

`BACK TO TOP <PropertyValueList_>`_

------------

