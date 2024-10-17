####################
ResearchProductGroup
####################

:Semantic name: core:ResearchProductGroup

:Display as: Core:research product group


------------

------------

Properties
##########

:Required: `context <context_heading_>`_, `hasPart <hasPart_heading_>`_
:Optional:

------------

.. _context_heading:

*******
context
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/context
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the common context for this research product group.

`BACK TO TOP <ResearchProductGroup_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | linked object array \(1-N\) of type
                | computation:ValidationTest \[TYPE_ERROR\], computation:ValidationTestVersion \[TYPE_ERROR\], computation:WorkflowRecipe \[TYPE_ERROR\], computation:WorkflowRecipeVersion \[TYPE_ERROR\], core:Dataset \[TYPE_ERROR\], core:DatasetVersion \[TYPE_ERROR\], core:MetaDataModel \[TYPE_ERROR\], core:MetaDataModelVersion \[TYPE_ERROR\], core:Model \[TYPE_ERROR\], core:ModelVersion \[TYPE_ERROR\], core:Software \[TYPE_ERROR\], core:SoftwareVersion \[TYPE_ERROR\], core:WebService \[TYPE_ERROR\], core:WebServiceVersion \[TYPE_ERROR\], publications:LivePaper \[TYPE_ERROR\], publications:LivePaperVersion \[TYPE_ERROR\], sands:BrainAtlas \[TYPE_ERROR\], sands:BrainAtlasVersion \[TYPE_ERROR\], sands:CommonCoordinateSpace \[TYPE_ERROR\] or sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\]
   :instructions: Add all research products (research product versions) that should be grouped under the given 'context'.

`BACK TO TOP <ResearchProductGroup_>`_

------------

