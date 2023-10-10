###################
openMINDS instances
###################

openMINDS instances should be provided as JSON-LD documents (file extension: ``*.jsonld``) and comply to the openMINDS schema type they reference. In the following we will demonstrate how to create openMINDS instances for simple examples.

Creating a minimal instance
###########################

Let us start be creating a "Person" instance. For this, we first need to check the constraints defined in the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_.

The "Person" schema demands only one required property, named `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#givenname>`_. The schema states also that for the property "givenName" only a single value of data type "string" is expected. The remaining properties of the schema are optional. Based on these constraints, let us define a minimal "Person" instance:

.. tabs::
   :caption: zaphod-beeblebrox.jsonld

   .. code-tab:: json
      :caption: v1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: v2

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
      }

Let us explain the meaning of ``"@context"``, ``"@vocab"``, ``"@id"``, and ``"@type"`` which are JSON-LD specific syntax keywords. 

The ``"@context"`` JSON-LD keyword can be used to map shortcut terms to internationalized resource identifiers (IRIs). In openMINDS, we use it to define the prefix of the global vocabulary for properties. For this, we combine it with the ``"@vocab"`` JSON-LD keyword to set a common prefix for all properties that do not match a JSON-LD keyword, an IRI, a compact IRI, or blank node identifier. A valid openMINDS JSON-LD can also be defined without stating ``"@context"`` and ``"@vocab"``, if all property names are expanded with the common vocabulary prefix. Our previously defined "Person" instance could therefore also look like this:

.. code-block:: json
   :caption: zaphod-beeblebrox.jsonld

   {
     "@id": "_:zaphod-beeblebrox",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
   }

The ``"@id"`` keyword is used to provide a unique, referable identifier for an instance (node) in a graph database. An ``"@id"`` has to be an IRI, a compact IRI or a blank node identifier. For your local openMINDS instances, we recommend to define a unique blank node identifier (prefix ``"_:"`` plus your identifier). For instances defined in the openMINDS libraries, we use openMINDS specific IRIs. Graph database management systems will typically use globally unique and persistent identifiers (e.g., a system-wide IRI prefix in combination with an universially unique identifier (UUID)).

The ``"@type"`` keyword in a JSONLD document is used to set the type of an instance (node) or the datatype of a typed value object within an instance. The ``"@type"`` keyword clearly identifies the metadata schema that should be used to validate the content of that instance or value object.


Link an instance with another instance
######################################

Instances within a graph database are linked. As example, let us link a "Person" instance with another instance. The "Person" schema tells us that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#contactinformation>`_ is actually a link (edge) to an instance of type "ContactInformation". Let us create an instance of type "ContactInformation" and link it from a "Person" instance. 

If we ckeck the constraints of the `"ContactInformation" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contactInformation.html>`_, we learn that an instance of this type only requires the property `"email" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contactInformation.html#email>`_ defined through a single value of data type "string". A respective "ContactInformation" instance could therefore look like this:

.. code-block:: json
   :caption: zaphod-beeblebrox_email.jsonld

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "_:zaphod-beeblebrox_email",
     "@type": "https://openminds.ebrains.eu/core/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

Further let us define again a "Person" instance. This time with the additional optional properties (`"familyName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#familyname>`_) which requires a simple string value and (`"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#contactInformation>`_) which requires a link to an instance of type "ContactInformation":

.. code-block:: json
   :caption: zaphod.jsonld

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
