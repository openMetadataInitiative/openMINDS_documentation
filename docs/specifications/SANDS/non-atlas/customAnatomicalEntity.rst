######################
CustomAnatomicalEntity
######################

https://openminds.ebrains.eu/sands/CustomAnatomicalEntity
---------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `name <name_heading_>`_
:Optional: `hasAnnotation <hasAnnotation_heading_>`_, `relatedUBERONTerm <relatedUBERONTerm_heading_>`_, `relationAssessment <relationAssessment_heading_>`_

------------

.. _hasAnnotation_heading:

hasAnnotation
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasAnnotation
   :value type: | embedded object array \(1-N\) of type
                | `CustomAnnotation <https://openminds.ebrains.eu/sands/CustomAnnotation>`_
   :instructions: Add all custom annotations which define this custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this custom anatomical entity.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _relatedUBERONTerm_heading:

relatedUBERONTerm
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedUBERONTerm
   :value type: | linked object of type
                | `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_or `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_
   :instructions: Add the related anatomical entity as defined by the UBERON ontology.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

.. _relationAssessment_heading:

relationAssessment
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relationAssessment
   :value type: | embedded object array \(1-N\) of type
                | `QualitativeRelationAssessment <https://openminds.ebrains.eu/sands/QualitativeRelationAssessment>`_or `QuantitativeRelationAssessment
                <https://openminds.ebrains.eu/sands/QuantitativeRelationAssessment>`_
   :instructions: Add all relations (qualitative or quantitative) of this custom anatomical entity to other anatomical entities.

`BACK TO TOP <CustomAnatomicalEntity_>`_

------------

