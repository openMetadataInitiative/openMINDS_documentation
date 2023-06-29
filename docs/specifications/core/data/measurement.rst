###########
Measurement
###########

*********************************************
https://openminds.ebrains.eu/core/Measurement
*********************************************

Structured information about a measurement performed during a scientific experiment.

------------

------------

**********
Properties
**********

:Required: `measuredQuantity <measuredQuantity_heading_>`_, `value <value_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `measuredWith <measuredWith_heading_>`_, `timestamp <timestamp_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concerning this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _measuredQuantity_heading:

measuredQuantity
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/measuredQuantity
   :value type: | linked object of type
                | `MeasuredQuantity <https://openminds.ebrains.eu/controlledTerms/MeasuredQuantity>`_
   :instructions: Add the quantity that was measured during this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _measuredWith_heading:

measuredWith
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/measuredWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage>`_, `ElectrodeUsage
                <https://openminds.ebrains.eu/ephys/ElectrodeUsage>`_, `PipetteUsage <https://openminds.ebrains.eu/ephys/PipetteUsage>`_or `SlicingDeviceUsage
                <https://openminds.ebrains.eu/specimenPrep/SlicingDeviceUsage>`_
   :instructions: Add the device that was used during this measurement.

`BACK TO TOP <Measurement_>`_

------------

.. _timestamp_heading:

timestamp
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/timestamp
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this measurement was made, formatted as '2023-02-07T16:00:00+00:00'.

`BACK TO TOP <Measurement_>`_

------------

.. _value_heading:

value
-----

Entry for a property.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/value
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_or `QuantitativeValueRange
                <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter all values that were measured at the same time and are of the same measured quantity.

`BACK TO TOP <Measurement_>`_

------------

