#############
Configuration
#############

:Semantic name: https://openminds.ebrains.eu/core/Configuration

Structured information about the properties or parameters of an entity or process.


------------

------------

Properties
##########

:Required: `configuration <configuration_heading_>`_, `format <format_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _configuration_heading:

*************
configuration
*************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/configuration
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the configuration in a simple text based format (e.g., JSON or YAML).

`BACK TO TOP <Configuration_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/data/contentType.html>`_
   :instructions: Add the content type of this configuration.

`BACK TO TOP <Configuration_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this configuration that may help you to find this instance more easily.

`BACK TO TOP <Configuration_>`_

------------

