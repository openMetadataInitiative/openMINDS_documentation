##############
ElectrodeArray
##############

*************************************************
https://openminds.ebrains.eu/sands/ElectrodeArray
*************************************************

Structured information on an electrode array.

------------

------------

**********
Properties
**********

:Required: `electrodes <electrodes_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_
:Optional:

------------

.. _electrodes_heading:

electrodes
----------

Elements in a semiconductor device that emits or collects electrons or holes or controls their movements.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/electrodes
   :value type: | linked object array \(2-N\) of type
                | `Electrode <https://openminds.ebrains.eu/sands/Electrode>`_
   :instructions: Add two or more electrodes which build this array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier used for this electrode array within the file it is stored in.

`BACK TO TOP <ElectrodeArray_>`_

------------

