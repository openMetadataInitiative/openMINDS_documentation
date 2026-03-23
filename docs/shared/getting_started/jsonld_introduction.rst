#############################
JSON-LD: minimal introduction
#############################

JSON-LD (JavaScript Object Notation for Linked Data) is a format for representing structured data as linked data using JSON.

In JSON-LD, data is expressed as a collection of objects that can be uniquely identified and linked to each other. This allows metadata to be represented as a graph of interconnected entities.

A minimal JSON-LD example could look like this:

.. code-block:: json

   {
     "@id": "_:example-person",
     "@type": "Person",
     "name": "Ada"
   }

In this example:

- ``"@id"`` defines a unique identifier for the object  
- ``"@type"`` specifies the type of the object  
- ``"name"`` is a simple property with a string value  

JSON-LD uses special keywords to define structure and semantics:

- ``"@id"``: identifies an object  
- ``"@type"``: defines the type of an object  
- ``"@context"``: defines how property names are interpreted  

The ``"@context"`` keyword is used to map property names to globally unique identifiers (IRIs). This allows different systems to interpret the same data consistently.

In JSON-LD, properties can either:

- contain simple values (e.g., strings or numbers), or  
- refer to other objects via their ``"@id"``  

This enables the creation of linked data structures.

The following chapters show how these concepts are used in openMINDS.
