############
SubjectState
############

https://openminds.ebrains.eu/core/SubjectState
----------------------------------------------

Structured information on a temporary state of a subject.

------------

------------

**********
Properties
**********

:Required: `ageCategory <ageCategory_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `age <age_heading_>`_, `handedness <handedness_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `pathology <pathology_heading_>`_, `weight <weight_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter additional remarks about the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _age_heading:

age
---

Time of life or existence at which some particular qualification, capacity or event arises.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/age
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Add the age of the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _ageCategory_heading:

ageCategory
-----------

Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ageCategory
   :value type: | linked object of type
                | `AgeCategory <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/ageCategory.html>`_
   :instructions: Add the age category of the subject in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _handedness_heading:

handedness
----------

Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/handedness
   :value type: | linked object of type
                | `Handedness <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/handedness.html>`_
   :instructions: Add the preferred hand of the subject in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen (set) state that may help you to more easily find it again.

`BACK TO TOP <SubjectState_>`_

------------

.. _pathology_heading:

pathology
---------

Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pathology
   :value type: | linked object array \(1-N\) of type
                | `Disease <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/disease.html>`_ or `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/diseaseModel.html>`_
   :instructions: Add the pathology of the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _weight_heading:

weight
------

Amount that a thing or being weighs.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/weight
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Add the weight of the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

