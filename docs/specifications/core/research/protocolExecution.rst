#################
ProtocolExecution
#################

***************************************************
https://openminds.ebrains.eu/core/ProtocolExecution
***************************************************

Structured information on a protocol execution.

------------

------------

**********
Properties
**********

:Required: `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `behavioralProtocol <behavioralProtocol_heading_>`_, `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_,
   `endTime <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign
   <preparationDesign_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _behavioralProtocol_heading:

behavioralProtocol
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/behavioralProtocol
   :value type: | linked object array \(1-N\) of type
                | `BehavioralProtocol <https://openminds.ebrains.eu/core/BehavioralProtocol>`_
   :instructions: Add all behavioral protocols that were performed during this protocol execution.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _customPropertySet_heading:

customPropertySet
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds.ebrains.eu/core/CustomPropertySet>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description of this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _endTime_heading:

endTime
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00'
      (time).

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _input_heading:

input
-----

Something or someone that is put into or participates in a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_, `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_, `SubjectGroupState
                <https://openminds.ebrains.eu/core/SubjectGroupState>`_, `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_,
                `TissueSampleCollectionState <https://openminds.ebrains.eu/core/TissueSampleCollectionState>`_, `TissueSampleState
                <https://openminds.ebrains.eu/core/TissueSampleState>`_, `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_or
                `CommonCoordinateSpaceVersion <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds.ebrains.eu/core/DatasetVersion>`_
   :instructions: Add the dataset version in which this activity was conducted.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _output_heading:

output
------

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_, `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_, `SubjectGroupState
                <https://openminds.ebrains.eu/core/SubjectGroupState>`_, `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_,
                `TissueSampleCollectionState <https://openminds.ebrains.eu/core/TissueSampleCollectionState>`_or `TissueSampleState
                <https://openminds.ebrains.eu/core/TissueSampleState>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _performedBy_heading:

performedBy
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds.ebrains.eu/computation/SoftwareAgent>`_or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _preparationDesign_heading:

preparationDesign
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationDesign
   :value type: | linked object of type
                | `PreparationType <https://openminds.ebrains.eu/controlledTerms/PreparationType>`_
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _protocol_heading:

protocol
--------

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds.ebrains.eu/core/Protocol>`_
   :instructions: Add all protocols used during this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _startTime_heading:

startTime
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00'
      (time).

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _studyTarget_heading:

studyTarget
-----------

Structure or function that was targeted within a study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds.ebrains.eu/controlledTerms/AuditoryStimulusType>`_, `BiologicalOrder
                <https://openminds.ebrains.eu/controlledTerms/BiologicalOrder>`_, `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_,
                `BreedingType <https://openminds.ebrains.eu/controlledTerms/BreedingType>`_, `CellCultureType
                <https://openminds.ebrains.eu/controlledTerms/CellCultureType>`_, `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Disease
                <https://openminds.ebrains.eu/controlledTerms/Disease>`_, `DiseaseModel <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_,
                `ElectricalStimulusType <https://openminds.ebrains.eu/controlledTerms/ElectricalStimulusType>`_, `GeneticStrainType
                <https://openminds.ebrains.eu/controlledTerms/GeneticStrainType>`_, `GustatoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/GustatoryStimulusType>`_, `Handedness <https://openminds.ebrains.eu/controlledTerms/Handedness>`_,
                `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_, `OlfactoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OlfactoryStimulusType>`_, `OpticalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OpticalStimulusType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `OrganismSystem
                <https://openminds.ebrains.eu/controlledTerms/OrganismSystem>`_, `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_,
                `SubcellularEntity <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `TactileStimulusType
                <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_, `TermSuggestion
                <https://openminds.ebrains.eu/controlledTerms/TermSuggestion>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `VisualStimulusType
                <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all study targets of this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

