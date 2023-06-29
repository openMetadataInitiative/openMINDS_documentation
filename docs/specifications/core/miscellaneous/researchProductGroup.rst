####################
ResearchProductGroup
####################

https://openminds.ebrains.eu/core/ResearchProductGroup
------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `context <context_heading_>`_, `hasPart <hasPart_heading_>`_
:Optional:

------------

.. _context_heading:

context
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/context
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the common context for this research product group.

`BACK TO TOP <ResearchProductGroup_>`_

------------

.. _hasPart_heading:

hasPart
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | linked object array \(1-N\) of type
                | `ValidationTest <https://openminds.ebrains.eu/computation/ValidationTest>`_, `ValidationTestVersion
                <https://openminds.ebrains.eu/computation/ValidationTestVersion>`_, `WorkflowRecipe <https://openminds.ebrains.eu/computation/WorkflowRecipe>`_,
                `WorkflowRecipeVersion <https://openminds.ebrains.eu/computation/WorkflowRecipeVersion>`_, `Dataset
                <https://openminds.ebrains.eu/core/Dataset>`_, `DatasetVersion <https://openminds.ebrains.eu/core/DatasetVersion>`_, `MetaDataModel
                <https://openminds.ebrains.eu/core/MetaDataModel>`_, `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_, `Model
                <https://openminds.ebrains.eu/core/Model>`_, `ModelVersion <https://openminds.ebrains.eu/core/ModelVersion>`_, `Software
                <https://openminds.ebrains.eu/core/Software>`_, `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_, `WebService
                <https://openminds.ebrains.eu/core/WebService>`_, `WebServiceVersion <https://openminds.ebrains.eu/core/WebServiceVersion>`_, `LivePaper
                <https://openminds.ebrains.eu/publications/LivePaper>`_, `LivePaperVersion <https://openminds.ebrains.eu/publications/LivePaperVersion>`_,
                `BrainAtlas <https://openminds.ebrains.eu/sands/BrainAtlas>`_, `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_,
                `CommonCoordinateSpace <https://openminds.ebrains.eu/sands/CommonCoordinateSpace>`_or `CommonCoordinateSpaceVersion
                <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_
   :instructions: Add all research products (research product versions) that should be grouped under the given 'context'.

`BACK TO TOP <ResearchProductGroup_>`_

------------

