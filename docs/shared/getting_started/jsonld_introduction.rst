#############################
JSON-LD: minimal introduction
#############################

JSON-LD (JavaScript Object Notation for Linked Data, see `JSON-LD 1.1 specification`_) is a format for representing structured data as Linked Data (see `Linked Data principles`_) using JSON.

In JSON-LD, data is expressed as a collection of objects that can be uniquely identified and linked to each other. This allows metadata to be represented as a graph of interconnected entities.

A minimal JSON-LD object
########################

The same JSON-LD object can be written in different syntactic forms. The following example shows a minimal object in three equivalent representations:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "https://schema.org/givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://schema.org/"
        },
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "schema": "https://schema.org/"
        },
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "schema:givenName": "Zaphod"
      }


These representations describe the same object. The expanded form uses full IRIs for all property names, while the compact forms use ``"@context"`` to shorten them. The underlying syntax is explained below.

JSON-LD syntax basics
#####################

The example above uses several JSON-LD keywords:

**"@id"**  
The keyword ``"@id"`` provides the identifier of an object. It can be a blank node identifier (e.g. ``"_:example-person"``) or a globally unique IRI. Within a metadata collection, each ``"@id"`` has to be unique.

**"@type"**  
The keyword ``"@type"`` specifies the type of an object. This is typically defined by a schema and expressed as an IRI (e.g. ``https://schema.org/Person``).

**"@context"**  
The keyword ``"@context"`` defines how property names are interpreted by mapping them to IRIs (Internationalized Resource Identifiers), e.g. ``https://schema.org/givenName``. Namespaces defined in ``"@context"`` are used to shorten these IRIs.

These representations differ in how namespaces are defined and used:

- **compact-1**: ``"@vocab"`` defines a default namespace, allowing properties to be written directly  
- **compact-2**: a custom prefix (e.g. ``"schema"``) defines a namespace used in property names  
- **expanded**: no ``"@context"`` is defined, so full IRIs must be used  

----

The following chapters show how these JSON-LD concepts are applied in openMINDS.

.. _JSON-LD 1.1 specification: https://www.w3.org/TR/json-ld11/
.. _Linked Data principles: https://www.w3.org/DesignIssues/LinkedData.html
