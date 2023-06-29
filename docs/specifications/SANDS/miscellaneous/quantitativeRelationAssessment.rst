##############################
QuantitativeRelationAssessment
##############################

https://openminds.ebrains.eu/sands/QuantitativeRelationAssessment
-----------------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `inRelationTo <inRelationTo_heading_>`_, `quantitativeOverlap <quantitativeOverlap_heading_>`_
:Optional: `criteria <criteria_heading_>`_

------------

.. _criteria_heading:

criteria
--------

Aspects or standards on which a judgement or decision is based.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteria
   :value type: | linked object of type
                | `ProtocolExecution <https://openminds.ebrains.eu/core/ProtocolExecution>`_
   :instructions: Add the protocol execution defining the criteria that were applied to determine this relation.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _inRelationTo_heading:

inRelationTo
------------

Reference to a related element.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inRelationTo
   :value type: | linked object of type
                | `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add the parcellation entity version to which the relation is described.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _quantitativeOverlap_heading:

quantitativeOverlap
-------------------

Numerical characterization of how much two things occupy the same space.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/quantitativeOverlap
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `QuantitativeValueRange <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the quantitative overlap between the two anatomical entities, preferably expressed in percentage.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

