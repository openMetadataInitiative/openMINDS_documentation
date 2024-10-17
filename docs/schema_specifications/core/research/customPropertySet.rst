#################
CustomPropertySet
#################

:Semantic name: core:CustomPropertySet

:Display as: Core:custom property set


------------

------------

Properties
##########

:Required: `context <context_heading_>`_, `dataLocation <dataLocation_heading_>`_, `relevantFor <relevantFor_heading_>`_
:Optional:

------------

.. _context_heading:

*******
context
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/context
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the common context for this custom property set.

`BACK TO TOP <CustomPropertySet_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | core:Configuration \[TYPE_ERROR\], core:File \[TYPE_ERROR\] or core:PropertyValueList \[TYPE_ERROR\]
   :instructions: Add the location of the data that define the custom property set for the given context (e.g., stored as file or other entities such as property-value lists).

`BACK TO TOP <CustomPropertySet_>`_

------------

.. _relevantFor_heading:

***********
relevantFor
***********

Reference to what or whom something or someone bears significance.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relevantFor
   :value type: | linked object of type
                | controlledTerms:AnalysisTechnique \[TYPE_ERROR\], controlledTerms:MRIPulseSequence \[TYPE_ERROR\], controlledTerms:MRIWeighting \[TYPE_ERROR\], controlledTerms:StimulationApproach \[TYPE_ERROR\], controlledTerms:StimulationTechnique \[TYPE_ERROR\] or controlledTerms:Technique \[TYPE_ERROR\]
   :instructions: Add the technique for which this custom property set is relevant.

`BACK TO TOP <CustomPropertySet_>`_

------------

