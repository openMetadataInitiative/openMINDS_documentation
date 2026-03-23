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
          "schema": "https://schema.org/"
        },
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "schema:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:example-person",
        "@type": "https://schema.org/Person",
        "https://schema.org/givenName": "Zaphod"
      }

These three representations describe the same object. They differ only in how property names are written. The differences are explained below.

JSON-LD keywords
################

The example above uses several JSON-LD keywords:

**"@context"**  
The keyword ``"@context"`` defines how property names are interpreted.

- In **compact-1**, ``"@vocab"`` sets a default IRI prefix for all properties  
- In **compact-2**, a custom prefix is defined and used in property names  
- In **expanded**, no ``"@context"`` is used; all property names are written as full IRIs  

**"@id"**  
The keyword ``"@id"`` provides the identifier of an object. It can be:

- an IRI  
- a compact IRI  
- a blank node identifier (e.g., ``"_:example-person"``)  

Within a metadata collection, each ``"@id"`` has to be unique.

**"@type"**  
The keyword ``"@type"`` specifies the type of an object. This is typically defined by a schema or vocabulary (e.g., ``https://schema.org/Person``).

Values and links
################

In JSON-LD, properties can either contain simple values or links to other objects.

Example of a simple value:

.. code-block:: json

   "givenName": "Zaphod"

Example of a link to another object:

.. code-block:: json

   "knows": {
     "@id": "_:another-person"
   }

In the second case, the property refers to another object via its identifier. This mechanism is used to connect objects into a linked data structure.

---

The following chapters show how these JSON-LD concepts are applied in openMINDS.
