#################
WorkflowExecution
#################

:Semantic name:: https://openminds.ebrains.eu/computation/WorkflowExecution

Structured information about an execution of a computational workflow.


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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | linked object of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/configuration.html>`_ or `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_
   :instructions: Add the configuration information for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _recipe_heading:

******
recipe
******

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/workflowRecipeVersion.html>`_
   :instructions: Add the workflow recipe version used for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _stage_heading:

*****
stage
*****

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stage
   :value type: | linked object array \(1-N\) of type
                | `DataAnalysis <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/dataAnalysis.html>`_, `DataCopy <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/dataCopy.html>`_, `GenericComputation <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/genericComputation.html>`_, `ModelValidation <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/modelValidation.html>`_, `Optimization <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/optimization.html>`_, `Simulation <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/simulation.html>`_ or `Visualization <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/visualization.html>`_
   :instructions: Add all stages that were performed in this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _startedBy_heading:

*********
startedBy
*********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_
   :instructions: Add the agent that started this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

