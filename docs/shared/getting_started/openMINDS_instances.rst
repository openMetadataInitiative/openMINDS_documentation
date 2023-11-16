###################
openMINDS instances
###################

openMINDS metadata instances should be provided as JSON-LD documents (file extension: ``*.jsonld``) and comply to the openMINDS schema type they reference. In the following we will demonstrate how to create openMINDS instances for simple examples.

Creating a minimal instance
###########################

Let us start be creating a "Person" instance. For this, we first need to check the constraints defined in the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_.

The "Person" schema demands only one required property, named `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#givenname>`_. The schema states also that for the property "givenName" only a single value of data type "string" is expected. The remaining properties of the schema are optional. Based on these constraints, let us define a minimal "Person" instance:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "vocab:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
      }

Let us explain the three versions for writing an openMINDS instance and the usage/meaning of JSON-LD specific syntax keywords (``"@context"``, ``"@vocab"``, ``"@id"``, and ``"@type"``), compact internationalized resource identifier (**compact IRI**), and blank node identifier (**blank node ID**). 

**"@context"**: The JSON-LD keyword ``"@context"`` can be used to map shortcut terms for internationalized resource identifiers (IRIs). In openMINDS, we use it to create a shortcut term for the common IRI prefix of the global vocabulary for properties by making use either of the JSON-LD keyword ``"@vocab"`` (cf. **compact-1**; preferred openMINDS formatting) or a compact IRI (cf. **compact-2**). You can also not make use of shortcut terms for the global vocabulary by explicitely stating the full namespace of each property (cf. **expanded**).

**"@vocab"**: The JSON-LD keyword ``"@vocab"`` can be used to set a common IRI prefix for all properties that do not match a JSON-LD keyword, an IRI, a compact IRI, or blank node ID.

**"@id"**: The JSON-LD keyword ``"@id"`` is used to provide a unique, referable identifier for an instance (node) in a graph database. An ``"@id"`` has to be an IRI, a compact IRI or a blank node ID. 

**"@type"**: The JSON-LD keyword ``"@type"`` is used to set the type of an instance (node) or a nested object within an instance, clearly identifying the metadata schema that should be used to validate the content of that instance or nested object.

**compact IRI**: A compact IRI has the form of ``"prefix:suffix"`` and is used as a way of simplifying full IRI namespaces (e.g., of properties) that have a common prefix. The common IRI prefix and the shortcut term used for it in the compact IRI have to be defined under ``"@context"`` (cf. **expanded**).

**blank node ID**: A blank node ID has the form of ``"_:suffix"`` and can be used to define a locally unique ``"@id"`` (cf. **compact-1**, **compact-2**, or **expanded**). Note that blank node identifier are not persistent or portable. In graph database management systems they are going to be replaced with globally unique and persistent identifiers (e.g., a system-wide IRI prefix in combination with an universially unique identifier (UUID)).

Link an instance with another instance
######################################

Instances within a graph database are linked through their unique identifiers. The "Person" schema tells us that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactinformation>`_ is actually expecting a link (edge) to another instance (object) of type "ContactInformation". Let us create an instance of type "ContactInformation" and link it from a "Person" instance. 

If we check the constraints of the `"ContactInformation" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contactInformation.html>`_, we learn that an instance of this type only requires the property `"email" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contactInformation.html#email>`_ defined through a single value of data type "string". A respective "ContactInformation" instance could therefore look like this:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "vocab:email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "https://openminds.ebrains.eu/vocab/email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
      }

Further let us extend our previous "Person" instance. This time with the additional optional properties `"familyName" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#familyname>`_ which requires a simple string value and `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactInformation>`_ which requires a link to an instance of type "ContactInformation":

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "familyName": "Beeblebrox",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "vocab:contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "vocab:familyName": "Beeblebrox",
        "vocab:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "https://openminds.ebrains.eu/vocab/familyName": "Beeblebrox",
        "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
      }

Embedding a typed object into an instance
#########################################

Instances within a graph database can also embed typed objects that are constrained by other metadata schemas than the one used for the parent instance. For our example, the "Person" schema tells us that the property `"affiliation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#affiliation>`_ is actually expecting 1 to N embedded objects of type "Affiliation".

If we check the constraints of the `"Affiliation" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html>`_, we learn that an instance of this type only requires the property `"memberOf" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html#memberof>`_ which requires a link to an instance of type "Consortium" or "Organization". Furthermore, we can check the constraints for the `"Consortium" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_ and the `"Organization" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ and learn that both only require the property "fullName" defined through a single value of data type "string".

In order to embed an object of type "Affiliation" into our "Person" instance we therefore have to first create at least one instance of type "Organization" or "Consortium":

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "fullName": "Heart of Gold Spacecraft Crew"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "vocab:fullName": "Heart of Gold Spacecraft Crew"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "https://openminds.ebrains.eu/vocab/fullName": "Heart of Gold Spacecraft Crew"
      }

Afterwards we can create a valid embedded "Affiliation" object inside our "Person" instance:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "familyName": "Beeblebrox",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "vocab:affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "vocab:memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "vocab:contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "vocab:familyName": "Beeblebrox",
        "vocab:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "https://openminds.ebrains.eu/vocab/memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "https://openminds.ebrains.eu/vocab/contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "https://openminds.ebrains.eu/vocab/familyName": "Beeblebrox",
        "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
      }
