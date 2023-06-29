##################
GenericComputation
##################

https://openminds.ebrains.eu/computation/GenericComputation
-----------------------------------------------------------

Structured information about a computation whose type is unknown or unspecified.

------------

------------

**********
Properties
**********

:Required: `environment <environment_heading_>`_, `input <input_heading_>`_, `output <output_heading_>`_, `startTime <startTime_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `endTime <endTime_heading_>`_, `launchConfiguration
   <launchConfiguration_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `recipe <recipe_heading_>`_, `resourceUsage
   <resourceUsage_heading_>`_, `startedBy <startedBy_heading_>`_, `status <status_heading_>`_, `studyTarget <studyTarget_heading_>`_, `tag <tag_heading_>`_,
   `technique <technique_heading_>`_, `wasInformedBy <wasInformedBy_heading_>`_

------------

.. _customPropertySet_heading:

customPropertySet
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds.ebrains.eu/core/CustomPropertySet>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _environment_heading:

environment
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/environment
   :value type: | linked object of type
                | `Environment <https://openminds.ebrains.eu/computation/Environment>`_ or `WebServiceVersion
                <https://openminds.ebrains.eu/core/WebServiceVersion>`_
   :instructions: Add the computational environment in which this computation was executed.

`BACK TO TOP <GenericComputation_>`_

------------

.. _input_heading:

input
-----

Something or someone that is put into or participates in a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds.ebrains.eu/computation/LocalFile>`_, `File <https://openminds.ebrains.eu/core/File>`_, `FileBundle
                <https://openminds.ebrains.eu/core/FileBundle>`_ or `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <GenericComputation_>`_

------------

.. _launchConfiguration_heading:

launchConfiguration
-------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/launchConfiguration
   :value type: | linked object of type
                | `LaunchConfiguration <https://openminds.ebrains.eu/computation/LaunchConfiguration>`_
   :instructions: Add the launch configuration of this computation (e.g., command-line arguments).

`BACK TO TOP <GenericComputation_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <GenericComputation_>`_

------------

.. _output_heading:

output
------

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds.ebrains.eu/computation/LocalFile>`_, `File <https://openminds.ebrains.eu/core/File>`_, `FileArchive
                <https://openminds.ebrains.eu/core/FileArchive>`_ or `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <GenericComputation_>`_

------------

.. _performedBy_heading:

performedBy
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds.ebrains.eu/computation/SoftwareAgent>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <GenericComputation_>`_

------------

.. _recipe_heading:

recipe
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds.ebrains.eu/computation/WorkflowRecipeVersion>`_
   :instructions: Add the workflow recipe version used for this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _resourceUsage_heading:

resourceUsage
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/resourceUsage
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter all resources used during this computation (e.g., core-hours or energy).

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _startedBy_heading:

startedBy
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds.ebrains.eu/computation/SoftwareAgent>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the agent that started this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _status_heading:

status
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/status
   :value type: | linked object of type
                | `ActionStatusType <https://openminds.ebrains.eu/controlledTerms/ActionStatusType>`_
   :instructions: Enter the current status of this computation.

`BACK TO TOP <GenericComputation_>`_

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
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_ or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all study targets of this activity.

`BACK TO TOP <GenericComputation_>`_

------------

.. _tag_heading:

tag
---

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/tag
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any custom tags for this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _technique_heading:

technique
---------

Method of accomplishing a desired aim.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_
   :instructions: Add all analysis techniques that were used in this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _wasInformedBy_heading:

wasInformedBy
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/wasInformedBy
   :value type: | linked object of type
                | `DataAnalysis <https://openminds.ebrains.eu/computation/DataAnalysis>`_, `DataCopy <https://openminds.ebrains.eu/computation/DataCopy>`_,
                `GenericComputation <https://openminds.ebrains.eu/computation/GenericComputation>`_, `ModelValidation
                <https://openminds.ebrains.eu/computation/ModelValidation>`_, `Optimization <https://openminds.ebrains.eu/computation/Optimization>`_,
                `Simulation <https://openminds.ebrains.eu/computation/Simulation>`_ or `Visualization <https://openminds.ebrains.eu/computation/Visualization>`_
   :instructions: Add another computation that sent data to this one during runtime.

`BACK TO TOP <GenericComputation_>`_

------------

