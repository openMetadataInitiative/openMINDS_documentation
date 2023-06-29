#############################
QualitativeRelationAssessment
#############################

****************************************************************
https://openminds.ebrains.eu/sands/QualitativeRelationAssessment
****************************************************************

------------

------------

**********
Properties
**********

:Required: `inRelationTo <inRelationTo_heading_>`_, `qualitativeOverlap <qualitativeOverlap_heading_>`_
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

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

.. _inRelationTo_heading:

inRelationTo
------------

Reference to a related element.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inRelationTo
   :value type: | linked object of type
                | `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_
   :instructions: Add the anatomical entity to which the relation is described.

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

.. _qualitativeOverlap_heading:

qualitativeOverlap
------------------

Semantic characterization of how much two things occupy the same space.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/qualitativeOverlap
   :value type: | linked object of type
                | `QualitativeOverlap <https://openminds.ebrains.eu/controlledTerms/QualitativeOverlap>`_
   :instructions: Add the qualitative overlap that best describes the relation between the two anatomical entities.

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

