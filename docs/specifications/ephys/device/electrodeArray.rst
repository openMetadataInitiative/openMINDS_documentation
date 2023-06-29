##############
ElectrodeArray
##############

https://openminds.ebrains.eu/ephys/ElectrodeArray
-------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `deviceType <deviceType_heading_>`_, `electrodeIdentifier <electrodeIdentifier_heading_>`_, `name <name_heading_>`_, `numberOfElectrodes
   <numberOfElectrodes_heading_>`_
:Optional: `conductorMaterial <conductorMaterial_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_,
   `insulatorMaterial <insulatorMaterial_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `intrinsicResistance
   <intrinsicResistance_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `owner <owner_heading_>`_, `serialNumber
   <serialNumber_heading_>`_

------------

.. _conductorMaterial_heading:

conductorMaterial
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/conductorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_, `ChemicalSubstance
                <https://openminds.ebrains.eu/chemicals/ChemicalSubstance>`_or `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_
   :instructions: Add the conductor material of this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short text describing this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _deviceType_heading:

deviceType
----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/deviceType
   :value type: | linked object of type
                | `DeviceType <https://openminds.ebrains.eu/controlledTerms/DeviceType>`_
   :instructions: Add the type of this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _digitalIdentifier_heading:

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_or `RRID <https://openminds.ebrains.eu/core/RRID>`_
   :instructions: Add the globally unique and persistent digital identifier of this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _electrodeIdentifier_heading:

electrodeIdentifier
-------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/electrodeIdentifier
   :value type: | string array \(2-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the identifiers for each electrode of this electrode array. Note that the number of identifiers should match the number of electrodes of
      the array as stated under 'numberOfElectrodes'.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _insulatorMaterial_heading:

insulatorMaterial
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/insulatorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_, `ChemicalSubstance
                <https://openminds.ebrains.eu/chemicals/ChemicalSubstance>`_or `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_
   :instructions: Add the insulator material of this electrode array.

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
   :instructions: Enter the identifier (or label) of this electrode array that is used within the corresponding data files to identify this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _intrinsicResistance_heading:

intrinsicResistance
-------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/intrinsicResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the intrinsic resistance of this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device that may help you to find this instance more easily.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _manufacturer_heading:

manufacturer
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/manufacturer
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the manufacturer (private or industrial) that constructed this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _numberOfElectrodes_heading:

numberOfElectrodes
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/numberOfElectrodes
   :value type: integer
   :instructions: Enter the number of electrodes that belong to this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _owner_heading:

owner
-----

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/owner
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that legally own this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _serialNumber_heading:

serialNumber
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/serialNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the serial number of this device.

`BACK TO TOP <ElectrodeArray_>`_

------------

