################
AtlasTerminology
################

:Semantic name:: https://openminds.ebrains.eu/sands/AtlasTerminology


------------

------------

Properties
##########

:Required: `anatomicalEntity <anatomicalEntity_heading_>`_, `fullName <fullName_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `definedIn <definedIn_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _anatomicalEntity_heading:

****************
anatomicalEntity
****************

Physical component of a body, organ, or tissue.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalEntity
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add all anatomical entities that belong to this atlas terminology.

`BACK TO TOP <AtlasTerminology_>`_

------------

.. _definedIn_heading:

*********
definedIn
*********

Reference to a file instance in which something is stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definedIn
   :value type: | linked object array \(1-N\) of type
                | `FileInstance <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/fileInstance.html>`_
   :instructions: Add one or several files in which this atlas terminology is stored in.

`BACK TO TOP <AtlasTerminology_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name for this atlas terminology.

`BACK TO TOP <AtlasTerminology_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (IRI) of the related ontological term matching this atlas terminology.

`BACK TO TOP <AtlasTerminology_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive short name for this atlas terminology.

`BACK TO TOP <AtlasTerminology_>`_

------------

