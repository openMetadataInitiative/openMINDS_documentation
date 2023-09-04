#################
Setting the terms
#################

**Metadata:** Data that provides contextual information on other data. In particular, metadata should provide information about data to facilitate their findability, accessibility, interoperability and reusability in accordance with the FAIR guiding principles for scientific data management and stewardship (cf. `Wilkinson et al. 2016 <https://doi.org/10.1038/sdata.2016.18>`_). Note that the distinction between metadata and data is not always clear and can be a matter of perspective.

**Property-value pair:** Fundamental structured (meta)data representation that consists of two elements: a value that can specify a (meta)data variable (e.g., "Homo sapiens") and a property defining the context of the value (e.g., "species"). Note that a value can be simple (e.g., string, number, array) or complex (e.g., property-value pair). Synonyms: attribute-value pair, field-value pair, key-value pair, name-value pair.

**Entity-property-value triple:** Fundamental structured (meta)data representation that consists of three elements: a value that can specify a (meta)data variable (e.g., "Jane"), a property defining the context of the value (e.g., "given name"), and an entity defining the context of the property (e.g., "person"). Note that the same entity can define the context of multiple properties (e.g., the properties "given name" and "family name" both belong to the entity "person"). Synonyms: entity-attribute-value triple, object-attribute-value triple, object-property-value triple, subject-attribute-value triple, subject-property-value triple.

**Metadata schema:** Specification of a set of required or optional properties and the type and number of expected values for each property for a certain entity (e.g., entity: "person", required property: "given name" with one expected value of type "string", optional property: "family name" with one expected value of type "string"). A metadata schema can be used as constrictive template to create consistently structured metadata instances for the same type of entity.

**Metadata instance:** Instanciation of metadata in form of property-value pairs or entity-property-value triples. Note that the information stored in an entity-property-value triple can be validated against a metadata schema of the respective entity type (e.g., a metadata instance of entity type "person" can be validated against the schema type "person").

**Metadata model:** Specification of multiple metadata schemas and the semantic relations that can be formed between instances constraint by these schemas (e.g., an instance of entity type "person" can be linked to an instance of entity type "dataset" with the relation definition "is curator of".

**Linked metadata instances:** Instanciation of metadata in form of entity-property-value triples that are equiped with unique identifiers in order to allow for non-ambiguous connections between the instances through those identifiers. A typical format for storing linked metadata instances is JSON-LD.
