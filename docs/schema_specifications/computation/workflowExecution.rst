#################
WorkflowExecution
#################

:Semantic name: computation:WorkflowExecution

:Display as: Computation:workflow execution


------------

------------

Properties
##########

:Required: `stages <stages_heading_>`_
:Optional: `configuration <configuration_heading_>`_, `recipe <recipe_heading_>`_, `stage <stage_heading_>`_, `startedBy <startedBy_heading_>`_

------------

.. _configuration_heading:

*************
configuration
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | linked object of type
                | core:Configuration \[TYPE_ERROR\] or core:File \[TYPE_ERROR\]
   :instructions: Add the configuration information for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _recipe_heading:

******
recipe
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recipe
   :value type: | linked object of type
                | computation:WorkflowRecipeVersion \[TYPE_ERROR\]
   :instructions: Add the workflow recipe version used for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _stage_heading:

*****
stage
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stage
   :value type: | linked object array \(1-N\) of type
                | computation:DataAnalysis \[TYPE_ERROR\], computation:DataCopy \[TYPE_ERROR\], computation:GenericComputation \[TYPE_ERROR\], computation:ModelValidation \[TYPE_ERROR\], computation:Optimization \[TYPE_ERROR\], computation:Simulation \[TYPE_ERROR\] or computation:Visualization \[TYPE_ERROR\]
   :instructions: Add all stages that were performed in this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _startedBy_heading:

*********
startedBy
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedBy
   :value type: | linked object of type
                | computation:SoftwareAgent \[TYPE_ERROR\] or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add the agent that started this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

