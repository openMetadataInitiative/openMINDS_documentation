##############################
QuantitativeRelationAssessment
##############################

:Semantic name: sands:QuantitativeRelationAssessment

:Display as: Sands:quantitative relation assessment


------------

------------

Properties
##########

:Required: `inRelationTo <inRelationTo_heading_>`_, `quantitativeOverlap <quantitativeOverlap_heading_>`_
:Optional: `criteria <criteria_heading_>`_

------------

.. _criteria_heading:

********
criteria
********

Aspects or standards on which a judgement or decision is based.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteria
   :value type: | linked object of type
                | core:ProtocolExecution \[TYPE_ERROR\]
   :instructions: Add the protocol execution defining the criteria that were applied to determine this relation.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _inRelationTo_heading:

************
inRelationTo
************

Reference to a related element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inRelationTo
   :value type: | linked object of type
                | sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add the parcellation entity version to which the relation is described.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _quantitativeOverlap_heading:

*******************
quantitativeOverlap
*******************

Numerical characterization of how much two things occupy the same space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/quantitativeOverlap
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the quantitative overlap between the two anatomical entities, preferably expressed in percentage.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

