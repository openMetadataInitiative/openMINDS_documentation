#############
SoftwareAgent
#############

******************************************************
https://openminds.ebrains.eu/computation/SoftwareAgent
******************************************************

Structured information about a piece of software or web service that can perform a task autonomously.

------------

------------

**********
Properties
**********

:Required: `name <name_heading_>`_, `software <software_heading_>`_
:Optional: `environment <environment_heading_>`_

------------

.. _environment_heading:

environment
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/environment
   :value type: | linked object of type
                | `Environment <https://openminds.ebrains.eu/computation/Environment>`_
   :instructions: Add the computational environment in which this software agent was running.

`BACK TO TOP <SoftwareAgent_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this software agent.

`BACK TO TOP <SoftwareAgent_>`_

------------

.. _software_heading:

software
--------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/software
   :value type: | linked object of type
                | `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_
   :instructions: Add the software version that is being run as this software agent.

`BACK TO TOP <SoftwareAgent_>`_

------------

