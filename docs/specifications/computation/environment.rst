###########
Environment
###########

:Semantic name:: https://openminds.ebrains.eu/computation/Environment

Structured information on the computer system or set of systems in which a computation is deployed and executed.


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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | linked object of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/configuration.html>`_
   :instructions: Add the configuration of this computational environment.

`BACK TO TOP <Environment_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short text describing this computational environment.

`BACK TO TOP <Environment_>`_

------------

.. _hardware_heading:

********
hardware
********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hardware
   :value type: | linked object of type
                | `HardwareSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/hardwareSystem.html>`_
   :instructions: Add the hardware system on which this computational environment runs.

`BACK TO TOP <Environment_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/software
   :value type: | linked object array \(1-N\) of type
                | `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/products/softwareVersion.html>`_
   :instructions: Add all software versions available in this computational environment.

`BACK TO TOP <Environment_>`_

------------

