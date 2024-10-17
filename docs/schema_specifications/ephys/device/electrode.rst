#########
Electrode
#########

:Semantic name: ephys:Electrode

:Display as: Ephys:electrode


------------

------------

Properties
##########

:Required: `deviceType <deviceType_heading_>`_, `name <name_heading_>`_
:Optional: `conductorMaterial <conductorMaterial_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `insulatorMaterial <insulatorMaterial_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `intrinsicResistance <intrinsicResistance_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `owner <owner_heading_>`_, `serialNumber <serialNumber_heading_>`_

------------

.. _conductorMaterial_heading:

*****************
conductorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/conductorMaterial
   :value type: | linked object of type
                | chemicals:ChemicalMixture \[TYPE_ERROR\], chemicals:ChemicalSubstance \[TYPE_ERROR\] or controlledTerms:MolecularEntity \[TYPE_ERROR\]
   :instructions: Add the conductor material of this electrode.

`BACK TO TOP <Electrode_>`_

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
   :instructions: Enter a short text describing this device.

`BACK TO TOP <Electrode_>`_

------------

.. _deviceType_heading:

**********
deviceType
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/deviceType
   :value type: | linked object of type
                | controlledTerms:DeviceType \[TYPE_ERROR\]
   :instructions: Add the type of this device.

`BACK TO TOP <Electrode_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | core:DOI \[TYPE_ERROR\] or core:RRID \[TYPE_ERROR\]
   :instructions: Add the globally unique and persistent digital identifier of this device.

`BACK TO TOP <Electrode_>`_

------------

.. _insulatorMaterial_heading:

*****************
insulatorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/insulatorMaterial
   :value type: | linked object of type
                | chemicals:ChemicalMixture \[TYPE_ERROR\], chemicals:ChemicalSubstance \[TYPE_ERROR\] or controlledTerms:MolecularEntity \[TYPE_ERROR\]
   :instructions: Add the insulator material of this electrode.

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
   :instructions: Enter the identifier (or label) of this electrode that is used within the corresponding data files to identify this electrode.

`BACK TO TOP <Electrode_>`_

------------

.. _intrinsicResistance_heading:

*******************
intrinsicResistance
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/intrinsicResistance
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the intrinsic resistance of this electrode.

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
   :instructions: Enter a lookup label for this device that may help you to find this instance more easily.

`BACK TO TOP <Electrode_>`_

------------

.. _manufacturer_heading:

************
manufacturer
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/manufacturer
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add the manufacturer (private or industrial) that constructed this device.

`BACK TO TOP <Electrode_>`_

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
   :instructions: Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer.

`BACK TO TOP <Electrode_>`_

------------

.. _owner_heading:

*****
owner
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/owner
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that legally own this device.

`BACK TO TOP <Electrode_>`_

------------

.. _serialNumber_heading:

************
serialNumber
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/serialNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the serial number of this device.

`BACK TO TOP <Electrode_>`_

------------

