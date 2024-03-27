################
ParameterSetting
################

:Semantic name: https://openminds.ebrains.eu/core/ParameterSetting

:Display as: Parameter setting

Structured information on a used parameter setting.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_, `relevantFor <relevantFor_heading_>`_, `value <value_heading_>`_
:Optional: `unit <unit_heading_>`_

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
   :instructions: Enter a description of this parameter setting.

`BACK TO TOP <ParameterSetting_>`_

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
   :instructions: Enter the name of this parameter setting.

`BACK TO TOP <ParameterSetting_>`_

------------

.. _relevantFor_heading:

***********
relevantFor
***********

Reference to what or whom something or someone bears significance.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relevantFor
   :value type: | linked object of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/behavioralTask.html>`_ or `Technique <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/technique.html>`_
   :instructions: Add the technique or behavioral task where this parameter setting is used in.

`BACK TO TOP <ParameterSetting_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement used for the value of this parameter setting.

`BACK TO TOP <ParameterSetting_>`_

------------

.. _value_heading:

*****
value
*****

Entry for a property.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/value
   :value type: | numberor string
                | formatting: undefined; singleline
   :instructions: Enter the value of this parameter setting.

`BACK TO TOP <ParameterSetting_>`_

------------

