#####################################
Instance guidelines for terminologies
#####################################

Instance libraries for terminologies follow schemas from the openMINDS controlledTerms module, which share a common conceptual structure.

To ensure consistent naming, definitions, and cross-references, the following additional guidelines apply across all terminology instance libraries.

Expected fields
###############

- Each instance contribution should at least define a ``name`` and a ``definition``.
- For specified libraries, preferred cross-references and/or ontology identifiers should be provided (see below).

Field conventions
#################

Name and identifier
===================

- The ``"@id"`` label is derived from the ``name``.
- Avoid abbreviations as primary names unless explicitly agreed.

Definition
==========

- Use a single-sentence structure: ``"[Term] is a [class] [qualifier] [characteristic/function]"``.
- Aim for ≤ 20 words where possible.
- Avoid circular definitions.
- Ensure the definition differentiates the term from others within the same class.
- Avoid examples unless explicitly agreed.

Description
===========

- Provide a standalone summary complementing the definition.
- Do not repeat the definition.
- Aim for < 300 words.
- External definitions may be included with citation where appropriate.

Synonyms
========

- Use exact synonyms, including commonly used abbreviations.

Ontologies and cross-references
===============================

- Reference matching `InterLex`_ terms where available (as preferred or additional ontology identifiers).
- Reference matching `INCF KnowledgeSpace`_ entries where available (as preferred or additional cross-references).
- Please use terms from selected preferred ontology or cross reference sources as specified in the `instance statistics`_.

.. _instance libraries: https://openminds.docs.om-i.org/en/latest/instance_libraries.html
.. _issue tracker: https://github.com/openMetadataInitiative/openMINDS_instances/issues
.. _linking openMINDS library instances: https://openminds.docs.om-i.org/en/latest/shared/getting_started/connecting_openMINDS_instances.html#linking-openminds-library-instances
.. _InterLex: https://scicrunch.org/scicrunch/interlex/search
.. _INCF KnowledgeSpace: https://knowledge-space.org/
.. _instance statistics: https://openmetadatainitiative.github.io/openMINDS_instances/
