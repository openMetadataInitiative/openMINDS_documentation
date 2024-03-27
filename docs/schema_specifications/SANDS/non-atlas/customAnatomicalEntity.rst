######################
CustomAnatomicalEntity
######################

:Semantic name: https://openminds.ebrains.eu/sands/CustomAnatomicalEntity

:Display as: Custom anatomical entity


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `hasAnnotation <hasAnnotation_heading_>`_, `relationAssessment <relationAssessment_heading_>`_

------------

.. _hasAnnotation_heading:

*************
hasAnnotation
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasAnnotation
   :value type: | linked object of type
                | `CustomAnnotation <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/non-atlas/customAnnotation.html>`_
   :instructions: Add the custom annotation which this custom anatomical entity defines.

`BACK TO TOP <CustomAnatomicalEntity_>`_

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
   :instructions: Enter a descriptive name for this custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _relationAssessment_heading:

******************
relationAssessment
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relationAssessment
   :value type: | embedded object array \(1-N\) of type
                | `QualitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/miscellaneous/qualitativeRelationAssessment.html>`_ or `QuantitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/miscellaneous/quantitativeRelationAssessment.html>`_
   :instructions: Add one or several relations of this custom anatomical entity to parcellation entities used in defined parcellation terminologies.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

