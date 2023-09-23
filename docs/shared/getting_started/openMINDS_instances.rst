###################
openMINDS instances
###################

openMINDS instances should be provided as JSON-LD documents (file extension: ``*.jsonld``) and comply to the openMINDS schema type they reference. In the following we will demonstrate how to create openMINDS instances for simple examples.

Creating a minimal instance
###########################

Let us start be creating a "Person" instance. For this, we first need to check the constraints defined in the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_.

The "Person" schema demands only one required property, named `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#givenname>`_. The schema states also that for the property "givenName" only a single value of data type "string" is expected. The remaining properties of the schema are optional and do not have to be specified in a valid openMINDS "Person" instance. Based on these constraints, let us define a minimal "Person" instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/person/12c42382-4c9c-4ee9-849e-b583a9f2ff25",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "givenName": "Zaphod"
   }

Let us explain in the following the meaning of ``"@context"``, ``"@vocab"``, ``"@id"``, and ``"@type"`` which are JSON-LD syntax keywords that can be part of any JSON-LD document. 

The ``"@context"`` keyword allows a JSON-LD document to use shortcut terms without losing accuracy. In openMINDS we particularly use it to define the prefix of the global vocabulary (``"@vocab"``) for properties (cf. . Generally, the ``"@vocab"`` keyword in a JSON-LD document sets a common prefix for all properties and types that do not match a term, an IRI, or a compact IRI. When unspecified in an openMINDS JSONLD, the property names have to be expanded with the prefix we specified for the ``"@vocab"`` keyword in our previous code block:

.. code-block:: json

   {
     "@id": "http://localhost/openminds/instance/person/12c42382-4c9c-4ee9-849e-b583a9f2ff25",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
   }

The ``"@id"`` keyword is used to uniquely identify an instance (node) in order to be able to reference this instance in a graph database. Ideally an ``"@id"`` keyword is defined as a globally unique and persistent identifier. In openMINDS, we typically combine a framework specific internationalized resource identifier (IRI) prefix with a version 4 universially unique identifier (UUID) which is a randomly generated 128 bit label.

The ``"@type"`` keyword in a JSONLD document is used to set the type of an instance (node) or the datatype of a typed value object within an instance. The ``"@type"`` keyword clearly identifies the metadata schema that should be used to validate the content of that instance or value object.


Link an instance with another instance
######################################

Let us now link the minimal "Person" instance we've created with metadata defined in an other instance. The "Person" schema tells us that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#contactinformation>`_ is actually an edge that should link to an instance of type "ContactInformation". We will therefore have to create a second instance of type "ContactInformation".

If we ckeck the constraints of the `"ContactInformation" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contactInformation.html>`_, we learn that an instance of this type only requires the property `"email" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contactInformation.html#email>`_ defined through a single value of data type "string". A respective "ContactInformation" instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/contactInformation/03ae13fe-73f3-4103-840c-1af75a9980cc",
     "@type": "https://openminds.ebrains.eu/core/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

Let us extend our "Person" instance with an value (single string) of an optional property (`"familyName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#familyname>`_) and the linkage to the "ContactInformation" instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/person/12c42382-4c9c-4ee9-849e-b583a9f2ff25",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "contactInformation": {
       "@id": "http://localhost/openminds/instance/contactInformation/03ae13fe-73f3-4103-840c-1af75a9980cc"
     },
     "familyName": "Beeblebrox",
     "givenName": "Zaphod"
   }
