#########
Recording
#########

********************************************
https://openminds.ebrains.eu/ephys/Recording
********************************************

------------

------------

**********
Properties
**********

:Required: `channel <channel_heading_>`_, `dataLocation <dataLocation_heading_>`_, `recordedWith <recordedWith_heading_>`_, `samplingFrequency
   <samplingFrequency_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `name <name_heading_>`_, `previousRecording
   <previousRecording_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concerning this recording.

`BACK TO TOP <Recording_>`_

------------

.. _channel_heading:

channel
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/channel
   :value type: | embedded object array \(1-N\) of type
                | `Channel <https://openminds.ebrains.eu/ephys/Channel>`_
   :instructions: Enter all channels used for this recording.

`BACK TO TOP <Recording_>`_

------------

.. _dataLocation_heading:

dataLocation
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | `File <https://openminds.ebrains.eu/core/File>`_or `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add the location of the file or file bundle in which the recorded data is stored.

`BACK TO TOP <Recording_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this recording that is used within the corresponding data files to identify this recording.

`BACK TO TOP <Recording_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this recording.

`BACK TO TOP <Recording_>`_

------------

.. _previousRecording_heading:

previousRecording
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/previousRecording
   :value type: | linked object of type
                | `Recording <https://openminds.ebrains.eu/ephys/Recording>`_
   :instructions: If this recording is part of a sequence of recordings (e.g., multiple repetitions or sweeps), add the recording preceding this recording.

`BACK TO TOP <Recording_>`_

------------

.. _recordedWith_heading:

recordedWith
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/recordedWith
   :value type: | linked object of type
                | `ElectrodeArrayUsage <https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage>`_, `ElectrodeUsage
                <https://openminds.ebrains.eu/ephys/ElectrodeUsage>`_, `PipetteUsage <https://openminds.ebrains.eu/ephys/PipetteUsage>`_or `SlicingDeviceUsage
                <https://openminds.ebrains.eu/specimenPrep/SlicingDeviceUsage>`_
   :instructions: Add the device used to generate this recording.

`BACK TO TOP <Recording_>`_

------------

.. _samplingFrequency_heading:

samplingFrequency
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/samplingFrequency
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the sampling frequency of this recording.

`BACK TO TOP <Recording_>`_

------------

