#################
CustomPropertySet
#################

***************************************************
https://openminds.ebrains.eu/core/CustomPropertySet
***************************************************

Structured information about properties of an entity that are not represented in an openMINDS schema.

------------

------------

**********
Properties
**********

:Required: `context <context_heading_>`_, `dataLocation <dataLocation_heading_>`_, `relevantFor <relevantFor_heading_>`_
:Optional:

------------

.. _context_heading:

context
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/context
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the common context for this custom property set.

`BACK TO TOP <CustomPropertySet_>`_

------------

.. _dataLocation_heading:

dataLocation
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | `Configuration <https://openminds.ebrains.eu/core/Configuration>`_, `File <https://openminds.ebrains.eu/core/File>`_or `PropertyValueList
                <https://openminds.ebrains.eu/core/PropertyValueList>`_
   :instructions: Add the location of the data that define the custom property set for the given context (e.g., stored as file or other entities such as
      property-value lists).

`BACK TO TOP <CustomPropertySet_>`_

------------

.. _relevantFor_heading:

relevantFor
-----------

Reference to what or whom something or someone bears siginificance.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relevantFor
   :value type: | linked object of type
                | `AnalysisTechnique <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_, `StimulationApproach
                <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_, `StimulationTechnique
                <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_or `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_
   :instructions: Add the technique for which this custom property set is relevant.

`BACK TO TOP <CustomPropertySet_>`_

------------

