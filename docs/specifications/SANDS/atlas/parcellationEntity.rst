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

:Required: `name <name_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `alternateName <alternateName_heading_>`_, `definition <definition_heading_>`_, `hasParent <hasParent_heading_>`_, `hasVersion <hasVersion_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `relatedUBERONTerm <relatedUBERONTerm_heading_>`_

------------

.. _abbreviation_heading:

abbreviation
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _alternateName_heading:

alternateName
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/alternateName
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any alternate names, including any alternative abbreviations, for this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _definition_heading:

definition
----------

Short, but precise statement of the meaning of a word, word group, sign or a symbol.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definition
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the definition for this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _hasParent_heading:

hasParent
---------

Reference to a parent object or legal person.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasParent
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_
   :instructions: Add all anatomical parent structures for this parcellation entity as defined within the corrsponding brain atlas.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _hasVersion_heading:

hasVersion
----------

Reference to variants of an original.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasVersion
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all versions of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this parcellation entity that may help you to find this instance more easily.

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
   :instructions: Enter the name of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _ontologyIdentifier_heading:

ontologyIdentifier
------------------

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _relatedUBERONTerm_heading:

relatedUBERONTerm
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedUBERONTerm
   :value type: | linked object of type
                | `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_ or `UBERONParcellation <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_
   :instructions: Add the related anatomical entity as defined by the UBERON ontology.

`BACK TO TOP <ParcellationEntity_>`_

------------

