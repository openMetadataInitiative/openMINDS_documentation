################
ElectrodeContact
################

https://openminds.ebrains.eu/sands/ElectrodeContact
---------------------------------------------------

Structured information on an electrode contact.

------------

------------

**********
Properties
**********

:Required: `coordinatePoint <coordinatePoint_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_
:Optional: `definedIn <definedIn_heading_>`_, `relatedRecording <relatedRecording_heading_>`_, `relatedStimulation <relatedStimulation_heading_>`_, `visualizedIn <visualizedIn_heading_>`_

------------

.. _coordinatePoint_heading:

coordinatePoint
---------------

Pair or triplet of numbers defining the position in a particular two- or three dimensional plane or space.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinatePoint
   :value type: | linked object of type
                | `CoordinatePoint <https://openminds.ebrains.eu/sands/CoordinatePoint>`_
   :instructions: Add the central coordinate of this electrode contact.

`BACK TO TOP <ElectrodeContact_>`_

------------

.. _definedIn_heading:

definedIn
---------

Reference to a file instance in which something is stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definedIn
   :value type: | linked object array \(1-N\) of type
                | `FileInstance <https://openminds.ebrains.eu/core/FileInstance>`_
   :instructions: Add one or several files in which the electrode contact is defined in.

`BACK TO TOP <ElectrodeContact_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier used for this electrode contact within the file it is stored in.

`BACK TO TOP <ElectrodeContact_>`_

------------

.. _relatedRecording_heading:

relatedRecording
----------------

Reference to the written, stored evidence of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedRecording
   :value type: | linked object array \(1-N\) of type
                | `FileInstance <https://openminds.ebrains.eu/core/FileInstance>`_
   :instructions: Add one or several files in which the recordings from this electrode contact were stored.

`BACK TO TOP <ElectrodeContact_>`_

------------

.. _relatedStimulation_heading:

relatedStimulation
------------------

Reference to the written, stored function used as a physiological stimulus.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedStimulation
   :value type: | linked object array \(1-N\) of type
                | `FileInstance <https://openminds.ebrains.eu/core/FileInstance>`_
   :instructions: Add one or several files in which the stimulations applied via this electrode contact were stored.

`BACK TO TOP <ElectrodeContact_>`_

------------

.. _visualizedIn_heading:

visualizedIn
------------

Reference to an image in which something is visible.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/visualizedIn
   :value type: | linked object array \(1-N\) of type
                | `Image <https://openminds.ebrains.eu/sands/Image>`_
   :instructions: Add one or several images in which the electrode contact is visualized in.

`BACK TO TOP <ElectrodeContact_>`_

------------

