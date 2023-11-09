########################
AnatomicalEntityRelation
########################

:Semantic name: https://openminds.ebrains.eu/sands/AnatomicalEntityRelation

Structured information on the relation between one anatomical entity and another.


------------

------------

Properties
##########

:Required: `criteriaQualityType <criteriaQualityType_heading_>`_, `inRelationTo <inRelationTo_heading_>`_, `qualitativeOverlap <qualitativeOverlap_heading_>`_
:Optional: `criteria <criteria_heading_>`_, `quantitativeOverlap <quantitativeOverlap_heading_>`_

------------

.. _criteria_heading:

********
criteria
********

Aspects or standards on which a judgement or decision is based.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteria
   :value type: | linked object of type
                | `ProtocolExecution <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/protocolExecution.html>`_
   :instructions: Add the protocol execution defining the criteria that were applied to determine this relation.

`BACK TO TOP <AnatomicalEntityRelation_>`_

------------

.. _criteriaQualityType_heading:

*******************
criteriaQualityType
*******************

Distinct class that defines how the judgement or decision was made for a particular criteria.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteriaQualityType
   :value type: | linked object of type
                | `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_
   :instructions: Add the quality type of the stated criteria used to determine this relation.

`BACK TO TOP <AnatomicalEntityRelation_>`_

------------

.. _inRelationTo_heading:

************
inRelationTo
************

Reference to a related element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inRelationTo
   :value type: | linked object of type
                | `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add the anatomical entity to which the relation is described.

`BACK TO TOP <AnatomicalEntityRelation_>`_

------------

.. _qualitativeOverlap_heading:

******************
qualitativeOverlap
******************

Semantic characterization of how much two things occupy the same space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/qualitativeOverlap
   :value type: | linked object of type
                | `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/qualitativeOverlap.html>`_
   :instructions: Add the qualitative overlap that best describes the relation between the two anatomical entities.

`BACK TO TOP <AnatomicalEntityRelation_>`_

------------

.. _quantitativeOverlap_heading:

*******************
quantitativeOverlap
*******************

Numerical characterization of how much two things occupy the same space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/quantitativeOverlap
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Add the quantitative overlap between the two anatomical entities preferably expressed in percentage.

`BACK TO TOP <AnatomicalEntityRelation_>`_

------------

