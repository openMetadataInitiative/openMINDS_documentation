#########
Electrode
#########

:Semantic name: https://openminds.ebrains.eu/sands/Electrode

:Display as: Electrode

Structured information on an electrode.


------------

------------

Properties
##########

:Required: `electrodeContact <electrodeContact_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _electrodeContact_heading:

****************
electrodeContact
****************

Not shielded part of a conductor that is used to establish electrical contact with a nonmetallic part of a circuit.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/electrodeContact
   :value type: | linked object array \(1-N\) of type
                | `ElectrodeContact <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/non-atlas/electrodeContact.html>`_
   :instructions: Add one or several electrical contacts of this electrode.

`BACK TO TOP <Electrode_>`_

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
   :instructions: Enter the identifier used for this electrode within the file it is stored in.

`BACK TO TOP <Electrode_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this electrode that may help you to more easily find it again.

`BACK TO TOP <Electrode_>`_

------------

