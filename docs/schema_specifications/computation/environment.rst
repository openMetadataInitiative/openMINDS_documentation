###########
Environment
###########

:Semantic name: computation:Environment

:Display as: Computation:environment


------------

------------

Properties
##########

:Required: `hardware <hardware_heading_>`_, `name <name_heading_>`_
:Optional: `configuration <configuration_heading_>`_, `description <description_heading_>`_, `software <software_heading_>`_

------------

.. _configuration_heading:

*************
configuration
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | linked object of type
                | core:Configuration \[TYPE_ERROR\]
   :instructions: Add the configuration of this computational environment.

`BACK TO TOP <Environment_>`_

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
   :instructions: Enter a short text describing this computational environment.

`BACK TO TOP <Environment_>`_

------------

.. _hardware_heading:

********
hardware
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hardware
   :value type: | linked object of type
                | computation:HardwareSystem \[TYPE_ERROR\]
   :instructions: Add the hardware system on which this computational environment runs.

`BACK TO TOP <Environment_>`_

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
   :instructions: Enter a descriptive name for this computational environment.

`BACK TO TOP <Environment_>`_

------------

.. _software_heading:

********
software
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/software
   :value type: | linked object array \(1-N\) of type
                | core:SoftwareVersion \[TYPE_ERROR\]
   :instructions: Add all software versions available in this computational environment.

`BACK TO TOP <Environment_>`_

------------

