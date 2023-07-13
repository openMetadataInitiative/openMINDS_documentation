#####################
LivePaperResourceItem
#####################

https://openminds.ebrains.eu/publications/LivePaperResourceItem
---------------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `IRI <IRI_heading_>`_, `hostedBy <hostedBy_heading_>`_, `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional:

------------

.. _IRI_heading:

IRI
---

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

.. _hostedBy_heading:

hostedBy
--------

Reference to an organization that provides facilities and services for something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hostedBy
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/organization.html>`_
   :instructions: Add the host organization of this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `LivePaperSection <https://openminds-documentation.readthedocs.io/en/latest/specifications/publications/livePaperSection.html>`_
   :instructions: Add the live paper section this live paper resource item is part of.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this live paper resource item.

`BACK TO TOP <LivePaperResourceItem_>`_

------------

