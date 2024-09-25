########
DataCopy
########

:Semantic name: https://openminds.ebrains.eu/computation/DataCopy

:Display as: Data copy


------------

------------

Properties
##########

:Required: `environment <environment_heading_>`_, `input <input_heading_>`_, `output <output_heading_>`_, `startTime <startTime_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `endTime <endTime_heading_>`_, `launchConfiguration <launchConfiguration_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `recipe <recipe_heading_>`_, `resourceUsage <resourceUsage_heading_>`_, `startedBy <startedBy_heading_>`_, `status <status_heading_>`_, `studyTarget <studyTarget_heading_>`_, `tag <tag_heading_>`_, `technique <technique_heading_>`_, `wasInformedBy <wasInformedBy_heading_>`_

------------

.. _customPropertySet_heading:

*****************
customPropertySet
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/customPropertySet.html>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <DataCopy_>`_

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

`BACK TO TOP <DataCopy_>`_

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

`BACK TO TOP <DataCopy_>`_

------------

.. _environment_heading:

***********
environment
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/environment
   :value type: | linked object of type
                | `Environment <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/environment.html>`_ or `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/webServiceVersion.html>`_
   :instructions: Add the computational environment in which this computation was executed.

`BACK TO TOP <DataCopy_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/localFile.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/validationTestVersion.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/modelVersion.html>`_ or `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <DataCopy_>`_

------------

.. _launchConfiguration_heading:

*******************
launchConfiguration
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/launchConfiguration
   :value type: | linked object of type
                | `LaunchConfiguration <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/launchConfiguration.html>`_
   :instructions: Add the launch configuration of this computation (e.g., command-line arguments).

`BACK TO TOP <DataCopy_>`_

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

`BACK TO TOP <DataCopy_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/localFile.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <DataCopy_>`_

------------

.. _performedBy_heading:

***********
performedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <DataCopy_>`_

------------

.. _recipe_heading:

******
recipe
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_
   :instructions: Add the workflow recipe version used for this computation.

`BACK TO TOP <DataCopy_>`_

------------

.. _resourceUsage_heading:

*************
resourceUsage
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/resourceUsage
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter all resources used during this computation (e.g., core-hours or energy).

`BACK TO TOP <DataCopy_>`_

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

`BACK TO TOP <DataCopy_>`_

------------

.. _startedBy_heading:

*********
startedBy
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add the agent that started this computation.

`BACK TO TOP <DataCopy_>`_

------------

.. _status_heading:

******
status
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/status
   :value type: | linked object of type
                | `ActionStatusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/actionStatusType.html>`_
   :instructions: Enter the current status of this computation.

`BACK TO TOP <DataCopy_>`_

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

`BACK TO TOP <DataCopy_>`_

------------

.. _tag_heading:

***
tag
***

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/tag
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any custom tags for this computation.

`BACK TO TOP <DataCopy_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/analysisTechnique.html>`_
   :instructions: Add all analysis techniques that were used in this computation.

`BACK TO TOP <DataCopy_>`_

------------

.. _wasInformedBy_heading:

*************
wasInformedBy
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/wasInformedBy
   :value type: | linked object of type
                | `DataAnalysis <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/dataAnalysis.html>`_, `DataCopy <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/dataCopy.html>`_, `GenericComputation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/genericComputation.html>`_, `ModelValidation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/modelValidation.html>`_, `Optimization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/optimization.html>`_, `Simulation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/simulation.html>`_ or `Visualization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/visualization.html>`_
   :instructions: Add another computation that sent data to this one during runtime.

`BACK TO TOP <DataCopy_>`_

------------

