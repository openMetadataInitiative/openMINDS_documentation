#######
Channel
#######

:Semantic name: ephys:Channel

:Display as: Ephys:channel


------------

------------

Properties
##########

:Required: `internalIdentifier <internalIdentifier_heading_>`_, `unit <unit_heading_>`_
:Optional:

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this channel that is used within the corresponding data files to identify this channel.

`BACK TO TOP <Channel_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/unit
   :value type: | linked object of type
                | controlledTerms:UnitOfMeasurement \[TYPE_ERROR\]
   :instructions: Add the unit of measurement for this channel.

`BACK TO TOP <Channel_>`_

------------

