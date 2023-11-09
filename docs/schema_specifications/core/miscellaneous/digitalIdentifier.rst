#################
DigitalIdentifier
#################

:Semantic name: https://openminds.ebrains.eu/core/DigitalIdentifier

Structured information on a digital identifier.


------------

------------

Properties
##########

:Required: `identifier <identifier_heading_>`_, `identifierSchema <identifierSchema_heading_>`_
:Optional: `howToCite <howToCite_heading_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for the resource this digital identifier stands for.

`BACK TO TOP <DigitalIdentifier_>`_

------------

.. _identifier_heading:

**********
identifier
**********

Term or code used to identify something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/identifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the digital identifier of a resource.

`BACK TO TOP <DigitalIdentifier_>`_

------------

.. _identifierSchema_heading:

****************
identifierSchema
****************

Standard for creating a particular identifier for something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/identifierSchema
   :value type: | linked object of type
                | `DigitalIdentifierSchema <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/digitalIdentifierSchema.html>`_
   :instructions: Add the used schema of this digital identifier.

`BACK TO TOP <DigitalIdentifier_>`_

------------

