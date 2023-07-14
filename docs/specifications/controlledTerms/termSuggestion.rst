##############
TermSuggestion
##############

:Semantic name:: https://openminds.ebrains.eu/controlledTerms/TermSuggestion


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `relatedTerminology <relatedTerminology_heading_>`_
:Optional: `definition <definition_heading_>`_, `description <description_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `terminology <terminology_heading_>`_

------------

.. _definition_heading:

**********
definition
**********

Short, but precise statement of the meaning of a word, word group, sign or a symbol.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definition
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter one sentence for defining this term.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short text describing this term.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Controlled term originating from a defined terminology.

`BACK TO TOP <TermSuggestion_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the related ontological term.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _terminology_heading:

***********
terminology
***********

Nomenclature for a particular field of study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/terminology
   :value type: | linked object of type
                | `Terminology <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/terminology.html>`_
   :instructions: Add the terminology in which the suggested term should be integrated in.

`BACK TO TOP <TermSuggestion_>`_

------------

