################
AnatomicalEntity
################

:Semantic name: https://openminds.ebrains.eu/sands/AnatomicalEntity

:Display as: Anatomical entity

Structured information on an anatomical entity.


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `hasParent <hasParent_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `otherAnatomicalRelation <otherAnatomicalRelation_heading_>`_

------------

.. _hasParent_heading:

*********
hasParent
*********

Reference to a parent object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasParent
   :value type: | linked object of type
                | `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add another anatomical entity representing the anatomical parent structure of this anatomical entity.

`BACK TO TOP <AnatomicalEntity_>`_

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
   :instructions: Enter a descriptive name for this anatomical entity based on anatomical location or characteristics.

`BACK TO TOP <AnatomicalEntity_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the ontological term matching this anatomical entity.

`BACK TO TOP <AnatomicalEntity_>`_

------------

.. _otherAnatomicalRelation_heading:

***********************
otherAnatomicalRelation
***********************

Reference to a related anatomical structure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherAnatomicalRelation
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalEntityRelation <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/anatomicalEntityRelation.html>`_
   :instructions: Add one or several relations of this anatomical entity to other anatomical entities that are used elsewhere to describe (roughly) the same anatomical location.

`BACK TO TOP <AnatomicalEntity_>`_

------------

