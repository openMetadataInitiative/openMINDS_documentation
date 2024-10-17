############
CellPatching
############

:Semantic name: ephys:CellPatching

:Display as: Ephys:cell patching


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `bathTemperature <bathTemperature_heading_>`_, `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `endTime <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_, `targetPosition <targetPosition_heading_>`_, `tissueBathSolution <tissueBathSolution_heading_>`_, `variation <variation_heading_>`_

------------

.. _bathTemperature_heading:

***************
bathTemperature
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/bathTemperature
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the temperature of the bath solution.

`BACK TO TOP <CellPatching_>`_

------------

.. _customPropertySet_heading:

*****************
customPropertySet
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | core:CustomPropertySet \[TYPE_ERROR\]
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object array \(1-N\) of type
                | ephys:ElectrodeArrayUsage \[TYPE_ERROR\], ephys:ElectrodeUsage \[TYPE_ERROR\], ephys:PipetteUsage \[TYPE_ERROR\] or specimenPrep:SlicingDeviceUsage \[TYPE_ERROR\]
   :instructions: Add all patch pipettes placed during this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _endTime_heading:

*******
endTime
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CellPatching_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | core:TissueSampleState \[TYPE_ERROR\] or core:SubjectState \[TYPE_ERROR\]
   :instructions: Add the state of the specimen that the device is being placed in or on during this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | core:DatasetVersion \[TYPE_ERROR\]
   :instructions: Add the dataset version in which this activity was conducted.

`BACK TO TOP <CellPatching_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <CellPatching_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | core:TissueSampleState \[TYPE_ERROR\] or core:SubjectState \[TYPE_ERROR\]
   :instructions: Add all states of the specimen(s) that the device was placed in or on as a result of this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _performedBy_heading:

***********
performedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | computation:SoftwareAgent \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _preparationDesign_heading:

*****************
preparationDesign
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationDesign
   :value type: | linked object of type
                | controlledTerms:PreparationType \[TYPE_ERROR\]
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/protocol
   :value type: | linked object array \(1-N\) of type
                | core:Protocol \[TYPE_ERROR\]
   :instructions: Add all protocols used during this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _startTime_heading:

*********
startTime
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CellPatching_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:BiologicalOrder \[TYPE_ERROR\], controlledTerms:BiologicalSex \[TYPE_ERROR\], controlledTerms:BreedingType \[TYPE_ERROR\], controlledTerms:CellCultureType \[TYPE_ERROR\], controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Disease \[TYPE_ERROR\], controlledTerms:DiseaseModel \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:GeneticStrainType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:Handedness \[TYPE_ERROR\], controlledTerms:MolecularEntity \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:OrganismSystem \[TYPE_ERROR\], controlledTerms:Species \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\], controlledTerms:TermSuggestion \[TYPE_ERROR\], controlledTerms:TissueSampleType \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], controlledTerms:VisualStimulusType \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all study targets of this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _targetPosition_heading:

**************
targetPosition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/targetPosition
   :value type: | embedded object of type
                | `AnatomicalTargetPosition <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/miscellaneous/anatomicalTargetPosition.html>`_
   :instructions: Enter the anatomical target position for the placement of the device.

`BACK TO TOP <CellPatching_>`_

------------

.. _tissueBathSolution_heading:

******************
tissueBathSolution
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/tissueBathSolution
   :value type: | linked object of type
                | chemicals:ChemicalMixture \[TYPE_ERROR\]
   :instructions: Add the chemical mixture used as bath solution during this activity.

`BACK TO TOP <CellPatching_>`_

------------

.. _variation_heading:

*********
variation
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/variation
   :value type: | linked object of type
                | controlledTerms:PatchClampVariation \[TYPE_ERROR\]
   :instructions: Add the patch-clamp variation used during this activity.

`BACK TO TOP <CellPatching_>`_

------------

