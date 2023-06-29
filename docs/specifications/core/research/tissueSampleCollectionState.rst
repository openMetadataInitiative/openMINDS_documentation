###########################
TissueSampleCollectionState
###########################

https://openminds.ebrains.eu/core/TissueSampleCollectionState
-------------------------------------------------------------

------------

------------

**********
Properties
**********

:Required:
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `age <age_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `pathology <pathology_heading_>`_,
   `weight <weight_heading_>`_

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

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _age_heading:

age
---

Time of life or existence at which some particular qualification, capacity or event arises.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/age
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Add the age of the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen (set) state that may help you to more easily find it again.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _pathology_heading:

pathology
---------

Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pathology
   :value type: | linked object array \(1-N\) of type
                | `Disease <https://openminds.ebrains.eu/controlledTerms/Disease>`_or `DiseaseModel
                <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_
   :instructions: Add the pathology of the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _weight_heading:

weight
------

Amount that a thing or being weighs.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/weight
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Add the weight of the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

