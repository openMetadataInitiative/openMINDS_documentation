################
LivePaperSection
################

https://openminds.ebrains.eu/publications/LivePaperSection
----------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_, `order <order_heading_>`_, `type <type_heading_>`_
:Optional: `description <description_heading_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description of this live paper section.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `LivePaperVersion <https://openminds.ebrains.eu/publications/LivePaperVersion>`_
   :instructions: Add the live paper version this live paper section is part of.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name (or title) of this live paper section.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _order_heading:

order
-----

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/order
   :value type: integer
   :instructions: Enter an integer that is used to sort this live paper section in ascending order with other live paper sections of the overarching live paper
      version.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _type_heading:

type
----

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Add the type of this live paper section (e.g., 'custom', 'generic', 'models', 'morphology', or 'traces').

`BACK TO TOP <LivePaperSection_>`_

------------

