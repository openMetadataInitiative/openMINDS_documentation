#############################
JSON-LD: minimal introduction
#############################

JSON-LD (JavaScript Object Notation for Linked Data) is a format for representing structured data as linked data using JSON.

In JSON-LD, data is expressed as a collection of objects that can be uniquely identified and linked to each other. This allows metadata to be represented as a graph of interconnected entities.

A minimal JSON-LD object
########################

The same JSON-LD object can be written in different syntactic forms. The following example shows a minimal object in three equivalent representations:

.. tabs:: instance-formatting

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
          "so": "https://schema.org/"
        },
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "so:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "https://schema.org/givenName": "Zaphod"
      }

These three representations describe the same object. They differ only in how property names are written. The differences are explained below.

JSON-LD syntax basics
#####################

The example above uses several JSON-LD keywords:

**"@context"**  
The keyword ``"@context"`` defines how property names are interpreted by mapping them to IRIs (Internationalized Resource Identifiers), which serve as globally unique identifiers, e.g. ``https://schema.org/givenName``. Namespaces defined in ``"@context"`` are used to shorten these IRIs and make JSON-LD more readable.

Depending on how the namespace is defined:

- **compact-1**: ``"@vocab"`` sets a default IRI prefix for all properties  
- **compact-2**: a custom prefix is defined and used in property names  
- **expanded**: no ``"@context"`` is used; all property names are written as full IRIs  

**"@id"**  
The keyword ``"@id"`` provides the identifier of an object. It can be:

- an IRI
- a compact IRI  
- a blank node identifier (e.g., ``"_:example-person"``)  

Within a metadata collection, each ``"@id"`` has to be unique.

**"@type"**  
The keyword ``"@type"`` specifies the type of an object. This is typically defined by a schema and expressed as an IRI (e.g. ``https://schema.org/Person``).

----

The following chapters show how these JSON-LD concepts are applied in openMINDS.
