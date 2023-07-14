#################
CustomPropertySet
#################

:Semantic name:: https://openminds.ebrains.eu/core/CustomPropertySet

Structured information about properties of an entity that are not represented in an openMINDS schema.


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

.. admonition:: specifications

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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/configuration.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_ or `PropertyValueList <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/propertyValueList.html>`_
   :instructions: Add the location of the data that define the custom property set for the given context (e.g., stored as file or other entities such as property-value lists).

`BACK TO TOP <CustomPropertySet_>`_

------------

.. _relevantFor_heading:

***********
relevantFor
***********

Reference to what or whom something or someone bears siginificance.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relevantFor
   :value type: | linked object of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/analysisTechnique.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationTechnique.html>`_ or `Technique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/technique.html>`_
   :instructions: Add the technique for which this custom property set is relevant.

`BACK TO TOP <CustomPropertySet_>`_

------------

