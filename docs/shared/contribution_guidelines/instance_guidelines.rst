###################
Instance guidelines
###################

openMINDS metadata instances represent concrete nodes in a metadata graph and follow the constraints defined by their respective schema types.

For selected schema types, openMINDS provides `instance libraries`_ that can be used as controlled or enumerated reference values.

Contributions to these instance libraries are welcome. To suggest modifications or propose new instances, please use the `issue tracker`_ of the openMINDS_instances repository on GitHub.

All contributions should follow the general guidelines and type-specific conventions outlined below.

General guidelines
##################

The following guidelines apply to all instances in openMINDS instance libraries.

Formatting
==========

- Instances are written in JSON-LD compact-1 format.
- Use 2 spaces per nested level for indentation (no tabs).
- Place a new line after commas ``,`` and after opening, non-empty braces ``{`` and brackets ``[``.
- Use 1 space after in-line colons ``:`` and commas ``,``.
- End the file with a trailing newline, in accordance with the POSIX standard.
- Use UTF-8 encoding for string-values.
- String-valued text fields may contain limited Markdown text formatting (e.g., hyperlinks, bold, italic).

Content
=======

- All properties defined by the schema should be specified. If a value is not yet defined, use ``null`` rather than omitting the property.
- All properties of an instance should be ordered alphabetically.
- The default language setting is US English.
- Provide citations as hyperlinks where applicable.

Instance identifiers
====================

Identifiers of openMINDS library instances (``"@id"``) are defined as IRIs to ensure global uniqueness within the openMINDS framework. 
Each identifier consists of an openMINDS-specific namespace prefix combined with a human-readable label.

The namespace prefix depends on the openMINDS version taking the following form (as introduced in `linking openMINDS library instances`_):

.. tabs:: instance-id-namespace

   .. code-tab:: text
      :caption: v4.0+

      https://openminds.om-i.org/instances/SCHEMA-NAME/

   .. code-tab:: text
      :caption: ≤ v3.0

      https://openminds.ebrains.eu/instances/SCHEMA-NAME/

The human-readable label is derived from a type-specific source value (e.g., name, abbreviation, or other identifying field) according to the following rules:

- remove spaces by applying lowerCamelCase  
- replace ``/`` with ``_``  
- preserve capitalization for proper names and abbreviations  
- retain unreserved characters: letters (A–Z, a–z), digits (0–9), and the characters ``-``, ``_``, ``.``, ``~``  

Instance guidelines for terminologies
#####################################

Instance libraries for terminologies follow schemas from the openMINDS controlledTerms module, which share a common conceptual structure.

To ensure consistent naming, definitions, and cross-references, the following additional guidelines apply across all terminology instance libraries.

Expected fields
===============

- Each instance contribution should at least define a ``name`` and a ``definition``.
- For specified libraries, preferred cross-references and/or ontology identifiers should be provided (see below).

Field conventions
=================

Name and identifier
-------------------

- The ``"@id"`` label is derived from the ``name``.
- Avoid abbreviations as primary names unless explicitly agreed.

Definition
----------

- Use a single-sentence structure: ``"[Term] is a [class] [qualifier] [characteristic/function]"``.
- Aim for ≤ 20 words where possible.
- Avoid circular definitions.
- Ensure the definition differentiates the term from others within the same class.
- Avoid examples unless explicitly agreed.

Description
-----------

- Provide a standalone summary complementing the definition.
- Do not repeat the definition.
- Aim for < 300 words.
- External definitions may be included with citation where appropriate.

Synonyms
--------

- Use exact synonyms, including commonly used abbreviations.

Ontologies and cross-references
------------------------------

- Reference matching InterLex terms where available (as preferred or additional ontology identifiers).
- Reference matching INCF KnowledgeSpace entries where available (as preferred or additional cross-references).
- Preferred ontologies by instance type: 

  - UBERON: ``AgeCategory``, ``AnatomicalCavity``, ``MuscularStructure``, ``NervousSystemStructure``, ``Organ``, ``TissueStructure``, ``VascularStructure``
  - CHEBI: ``ChemicalMixture``, ``MolecularEntity``

- Preferred cross-references by instance type:

  - Wikidata: ``SovereignState``
  - PubChem: ``ChemicalMixture``, ``MolecularEntity``

.. _instance libraries: https://openminds.docs.om-i.org/en/latest/instance_libraries.html
.. _issue tracker: https://github.com/openMetadataInitiative/openMINDS_instances/issues
.. _linking openMINDS library instances: https://openminds.docs.om-i.org/en/latest/shared/getting_started/connecting_openMINDS_instances.html#linking-openminds-library-instances
.. _InterLex: https://scicrunch.org/scicrunch/interlex/dashboard
