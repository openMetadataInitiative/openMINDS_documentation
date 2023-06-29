#############
SlicingDevice
#############

https://openminds.ebrains.eu/specimenPrep/SlicingDevice
-------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `deviceType <deviceType_heading_>`_, `name <name_heading_>`_
:Optional: `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `owner <owner_heading_>`_, `serialNumber <serialNumber_heading_>`_

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

`BACK TO TOP <SlicingDevice_>`_

------------

.. _deviceType_heading:

deviceType
----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/deviceType
   :value type: | linked object of type
                | `DeviceType <https://openminds.ebrains.eu/controlledTerms/DeviceType>`_
   :instructions: Add the type of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _digitalIdentifier_heading:

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_ or `RRID <https://openminds.ebrains.eu/core/RRID>`_
   :instructions: Add the globally unique and persistent digital identifier of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device that may help you to find this instance more easily.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _manufacturer_heading:

manufacturer
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/manufacturer
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the manufacturer (private or industrial) that constructed this device.

`BACK TO TOP <SlicingDevice_>`_

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

`BACK TO TOP <SlicingDevice_>`_

------------

.. _owner_heading:

owner
-----

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/owner
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that legally own this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _serialNumber_heading:

serialNumber
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/serialNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the serial number of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

