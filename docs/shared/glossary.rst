########
Glossary
########

.. glossary::

   metadata
      Data that provides contextual information on other data. In particular, metadata should provide information about data to facilitate their findability, accessibility, interoperability and reusability in accordance with the FAIR guiding principles for scientific data management and stewardship (cf. `Wilkinson et al. 2016 <https://doi.org/10.1038/sdata.2016.18>`_). The distinction between metadata and data is a matter of perspective. For this reason, 'metadata' are often also referred to by simply using the term 'data' or '(meta)data'.

   property-value pair
      Fundamental structured (meta)data representation that consists of two elements: a value that can specify a (meta)data variable (e.g., 'Homo sapiens') and a property defining the context of the value (e.g., 'species'). Note that a value can be simple (e.g., string, number, array) or complex (e.g., property-value pair). Synonyms: attribute-value pair, field-value pair, key-value pair, name-value pair.

   entity-property-value triple
      Fundamental structured (meta)data representation that consists of three elements: a value that can specify a (meta)data variable (e.g., 'Jane'), a property defining the context of the value (e.g., 'given name'), and an entity defining the context of the property (e.g., 'Person'). Note that entity types are typically capitalized and properties remain in lower case. Moreover, note that the same entity can define the context of multiple properties (e.g., the properties 'given name' and 'family name' both belong to the entity 'Person'). Synonyms: entity-attribute-value triple, object-attribute-value triple, object-property-value triple, subject-attribute-value triple, subject-property-value triple.

   metadata instance
      Instantiation of metadata in form of property-value pairs or entity-property-value triples. There are various file formats used to instantiated metadata of different data type (tables or associative arrays). A typical metadata table format is CSV and a typical metadata associative array format is JSON.

   metadata schema
      Specification of a set of required or optional properties and the type and number of expected values for each property for a certain entity type (schema type). For example, the schema type 'Person', defines that the property 'given name' is required with one expected value of type 'string', and the property 'family name' is optional with also one expected value of type 'string'. A metadata schema is used as constrictive template to create consistently structured metadata instances for the same type of entity.

   metadata model
      Specification of multiple metadata schemas and the semantic relations that can be formed between instances constraint by these schemas. For example, the schema 'Dataset' defines that an instance of type 'Dataset' can be linked to multiple instances of type 'Person' through the relation definition 'has authors'.

   linked metadata instances
      Instantiation of metadata in form of entity-property-value triples that are equipped with unique identifiers in order to allow for non-ambiguous connections between the instances through those identifiers. A typical format for storing linked metadata instances is JSON-LD. The type and unique identifier of a JSON-LD instance are always defined under the properties `'@type'` and `'@id'`.

   graph database
      Database that uses semantically queryable graph structures, where nodes (metadata instances) represent conceptual entities with property-value pairs and edges represent the relationships between the nodes. Graph databases can be designed schemaless, and are therefore often used for highly heterogeneous data collections. However, most graph database management systems use metadata models to constrain and validate the nodes and edges to increase the robustness of data queries. 
