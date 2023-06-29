############
CellPatching
############

***********************************************
https://openminds.ebrains.eu/ephys/CellPatching
***********************************************

------------

------------

**********
Properties
**********

:Required: `device <device_heading_>`_, `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `bathTemperature <bathTemperature_heading_>`_, `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `endTime
   <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_,
   `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_, `targetPosition <targetPosition_heading_>`_, `tissueBathSolution
   <tissueBathSolution_heading_>`_, `variation <variation_heading_>`_

------------

.. _bathTemperature_heading:

bathTemperature
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/bathTemperature
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the temperature of the bath solution.

`BACK TO TOP <CellPatching_>`_

------------

.. _customPropertySet_heading:

customPropertySet
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds.ebrains.eu/core/CustomPropertySet>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

------------

.. _device_heading:

device
------

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object array \(1-N\) of type
                | `ElectrodeArrayUsage <https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage>`_, `ElectrodeUsage
                <https://openminds.ebrains.eu/ephys/ElectrodeUsage>`_, `PipetteUsage <https://openminds.ebrains.eu/ephys/PipetteUsage>`_or `SlicingDeviceUsage
                <https://openminds.ebrains.eu/specimenPrep/SlicingDeviceUsage>`_
   :instructions: Add all patch pipettes placed during this activity.

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

------------

.. _input_heading:

input
-----

Something or someone that is put into or participates in a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_or `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_
   :instructions: Add the state of the specimen that the device is being placed in or on during this activity.

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <CellPatching_>`_

------------

.. _output_heading:

output
------

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_or `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_
   :instructions: Add all states of the specimen(s) that the device was placed in or on as a result of this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _performedBy_heading:

performedBy
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds.ebrains.eu/computation/SoftwareAgent>`_or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _preparationDesign_heading:

preparationDesign
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationDesign
   :value type: | linked object of type
                | `PreparationType <https://openminds.ebrains.eu/controlledTerms/PreparationType>`_
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

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

`BACK TO TOP <CellPatching_>`_

------------

.. _targetPosition_heading:

targetPosition
--------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/targetPosition
   :value type: | embedded object of type
                | `AnatomicalTargetPosition <https://openminds.ebrains.eu/sands/AnatomicalTargetPosition>`_
   :instructions: Enter the anatomical target position for the placement of the device.

`BACK TO TOP <CellPatching_>`_

------------

.. _tissueBathSolution_heading:

tissueBathSolution
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/tissueBathSolution
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_
   :instructions: Add the chemical mixture used as bath solution during this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _variation_heading:

variation
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/variation
   :value type: | linked object of type
                | `PatchClampVariation <https://openminds.ebrains.eu/controlledTerms/PatchClampVariation>`_
   :instructions: Add the patch-clamp variation used during this activity.

`BACK TO TOP <CellPatching_>`_

------------

