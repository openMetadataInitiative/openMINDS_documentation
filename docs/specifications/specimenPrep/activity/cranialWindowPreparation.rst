########################
CranialWindowPreparation
########################

:Semantic name: https://openminds.ebrains.eu/specimenPrep/CranialWindowPreparation


------------

------------

Properties
##########

:Required: `constructionType <constructionType_heading_>`_, `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `dimension <dimension_heading_>`_, `endTime <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `reinforcementType <reinforcementType_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _constructionType_heading:

****************
constructionType
****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/constructionType
   :value type: | linked object of type
                | `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cranialWindowConstructionType.html>`_
   :instructions: Add the construction type of the cranial window.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _customPropertySet_heading:

*****************
customPropertySet
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/customPropertySet.html>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _dimension_heading:

*********
dimension
*********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dimension
   :value type: | embedded object of type
                | `Circle <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/mathematicalShapes/circle.html>`_, `Ellipse <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/mathematicalShapes/ellipse.html>`_ or `Rectangle <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/mathematicalShapes/rectangle.html>`_
   :instructions: Enter the dimension of the cranial window by defining its mathematical shape.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _endTime_heading:

*******
endTime
*******

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectState.html>`_
   :instructions: Add the state of the subject which received the cranial window before this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version in which this activity was conducted.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectState.html>`_
   :instructions: Add the state of the subject which received the cranial window as a result of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _performedBy_heading:

***********
performedBy
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _preparationDesign_heading:

*****************
preparationDesign
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationDesign
   :value type: | linked object of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/preparationType.html>`_
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/protocol.html>`_
   :instructions: Add all protocols used during this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _reinforcementType_heading:

*****************
reinforcementType
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/reinforcementType
   :value type: | linked object of type
                | `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cranialWindowReinforcementType.html>`_
   :instructions: Add the reinforcement type of the cranial window.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _startTime_heading:

*********
startTime
*********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/electricalStimulusType.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSystem.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tactileStimulusType.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/termSuggestion.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/visualStimulusType.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all study targets of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

