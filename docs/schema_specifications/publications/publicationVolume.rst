#################
PublicationVolume
#################

:Semantic name: publications:PublicationVolume

:Display as: Publications:publication volume


------------

------------

Properties
##########

:Required: `isPartOf <isPartOf_heading_>`_, `volumeNumber <volumeNumber_heading_>`_
:Optional:

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | publications:Periodical \[TYPE_ERROR\]
   :instructions: Add the periodical this publication volume is part of.

`BACK TO TOP <PublicationVolume_>`_

------------

.. _volumeNumber_heading:

************
volumeNumber
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/volumeNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the volume number of this publication volume.

`BACK TO TOP <PublicationVolume_>`_

------------

