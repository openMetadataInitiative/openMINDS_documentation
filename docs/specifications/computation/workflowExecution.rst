#################
WorkflowExecution
#################

https://openminds.ebrains.eu/computation/WorkflowExecution
----------------------------------------------------------

Structured information about an execution of a computational workflow.

------------

------------

**********
Properties
**********

:Required: `stages <stages_heading_>`_
:Optional: `configuration <configuration_heading_>`_, `recipe <recipe_heading_>`_, `stage <stage_heading_>`_, `startedBy <startedBy_heading_>`_

------------

.. _configuration_heading:

configuration
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | linked object of type
                | `Configuration <https://openminds.ebrains.eu/core/Configuration>`_ or `File <https://openminds.ebrains.eu/core/File>`_
   :instructions: Add the configuration information for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _recipe_heading:

recipe
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds.ebrains.eu/computation/WorkflowRecipeVersion>`_
   :instructions: Add the workflow recipe version used for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _stage_heading:

stage
-----

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stage
   :value type: | linked object array \(1-N\) of type
                | `DataAnalysis <https://openminds.ebrains.eu/computation/DataAnalysis>`_, `DataCopy <https://openminds.ebrains.eu/computation/DataCopy>`_,
                `GenericComputation <https://openminds.ebrains.eu/computation/GenericComputation>`_, `ModelValidation
                <https://openminds.ebrains.eu/computation/ModelValidation>`_, `Optimization <https://openminds.ebrains.eu/computation/Optimization>`_,
                `Simulation <https://openminds.ebrains.eu/computation/Simulation>`_ or `Visualization <https://openminds.ebrains.eu/computation/Visualization>`_
   :instructions: Add all stages that were performed in this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _startedBy_heading:

startedBy
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds.ebrains.eu/computation/SoftwareAgent>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the agent that started this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

