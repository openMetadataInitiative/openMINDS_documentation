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
                | `ValidationTest <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/validationTest.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/validationTestVersion.html>`_, `WorkflowRecipe <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipe.html>`_, `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_, `Dataset <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/software.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/softwareVersion.html>`_, `WebService <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/webService.html>`_, `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/webServiceVersion.html>`_, `LivePaper <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/publications/livePaper.html>`_, `LivePaperVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/publications/livePaperVersion.html>`_, `BrainAtlas <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/brainAtlas.html>`_, `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_, `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add all research products (research product versions) that should be grouped under the given 'context'.

`BACK TO TOP <ResearchProductGroup_>`_

------------

