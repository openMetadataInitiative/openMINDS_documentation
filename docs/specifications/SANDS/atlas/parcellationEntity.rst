##################
ParcellationEntity
##################

https://openminds.ebrains.eu/sands/ParcellationEntity
-----------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_, `relatedUBERONTerm <relatedUBERONTerm_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `hasAnnotation <hasAnnotation_heading_>`_, `hasParent <hasParent_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `relationAssessment <relationAssessment_heading_>`_

------------

.. _hasAnnotation_heading:

hasAnnotation
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasAnnotation
   :value type: | linked object of type
                | `AtlasAnnotation <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/SANDS/atlas/atlasAnnotation.html>`_
   :instructions: Add the atlas annotation which this parcellation entity defines.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _hasParent_heading:

hasParent
---------

Reference to a parent object or legal person.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasParent
   :value type: | linked object of type
                | `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/SANDS/atlas/parcellationEntity.html>`_
   :instructions: Add for this parcellation entity the defined anatomical parent structure.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `ParcellationTerminology <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/SANDS/atlas/parcellationTerminology.html>`_
   :instructions: Add one or several parcellation terminologies to which this parcellation entity belongs.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name for this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _ontologyIdentifier_heading:

ontologyIdentifier
------------------

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the ontological term matching this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _relatedUBERONTerm_heading:

relatedUBERONTerm
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedUBERONTerm
   :value type: | linked object of type
                | `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/controlledTerms/UBERONParcellation.html>`_
   :instructions: Add the related UBERON parcellation term.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _relationAssessment_heading:

relationAssessment
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relationAssessment
   :value type: | embedded object array \(1-N\) of type
                | `QualitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/SANDS/miscellaneous/qualitativeRelationAssessment.html>`_ or `QuantitativeRelationAssessment <https://openminds-documentation.readthedocs.io/en/v2.0/specifications/SANDS/miscellaneous/quantitativeRelationAssessment.html>`_
   :instructions: Add one or several relations of this parcellation entity to parcellation entities of other parcellation terminologies.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _versionIdentifier_heading:

versionIdentifier
-----------------

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _versionInnovation_heading:

versionInnovation
-----------------

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description of the novelties/peculiarities of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

