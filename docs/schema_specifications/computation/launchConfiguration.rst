###################
LaunchConfiguration
###################

:Semantic name: computation:LaunchConfiguration

:Display as: Computation:launch configuration


------------

------------

Properties
##########

:Required: `executable <executable_heading_>`_
:Optional: `argument <argument_heading_>`_, `description <description_heading_>`_, `environmentVariable <environmentVariable_heading_>`_, `name <name_heading_>`_

------------

.. _argument_heading:

********
argument
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/argument
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all command line arguments for this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

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
   :instructions: Enter a short text describing this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

.. _environmentVariable_heading:

*******************
environmentVariable
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/environmentVariable
   :value type: | linked object of type
                | core:PropertyValueList \[TYPE_ERROR\]
   :instructions: Add any environment variables defined by this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

.. _executable_heading:

**********
executable
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/executable
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the path to the command-line executable.

`BACK TO TOP <LaunchConfiguration_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

