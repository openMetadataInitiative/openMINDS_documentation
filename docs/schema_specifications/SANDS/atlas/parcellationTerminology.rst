#######################
ParcellationTerminology
#######################

:Semantic name: sands:ParcellationTerminology

:Display as: Sands:parcellation terminology


------------

------------

Properties
##########

:Required: `hasEntity <hasEntity_heading_>`_
:Optional: `dataLocation <dataLocation_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object array \(1-N\) of type
                | core:File \[TYPE_ERROR\]
   :instructions: Add the location of all files in which this parcellation terminology is stored.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _hasEntity_heading:

*********
hasEntity
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasEntity
   :value type: | linked object array \(1-N\) of type
                | sands:ParcellationEntity \[TYPE_ERROR\]
   :instructions: Add all parcellation entities which belong to this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

