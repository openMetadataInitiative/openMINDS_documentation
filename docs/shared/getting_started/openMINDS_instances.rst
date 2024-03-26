###################
openMINDS instances
###################

openMINDS metadata instances should be provided as JSON-LD documents (file extension: ``*.jsonld``) and comply to the openMINDS schema type they reference. In the following we will explain how openMINDS instances look like for simple examples.

Creating a minimal instance
###########################

Let us start by looking at a simple "Person" instance which has to be designed according to the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_.

If you inspect the "Person" schema, you learn that only the property `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#givenname>`_ is required. Furthermore, the schema demands that the property "givenName" can only state a single value of data type "string". The remaining properties of the schema are optional. 

Based on these constraints, a minimal "Person" instance could look like this:

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
          "om": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "om:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "https://openminds.ebrains.eu/vocab/givenName": "Zaphod"
      }

As you can see, you can use three syntaxes (**"compact-1"**, **"compact-2"**, and **"expanded"**) for an openMINDS_instance. In the following, we will explain these syntaxes together with their usage/meaning of the JSON-LD specific keywords (``"@context"``, ``"@vocab"``, ``"@id"``, and ``"@type"``). 

**"@context"**: The JSON-LD keyword ``"@context"`` has to be specified when using one of the compact JSON-LD syntaxes (**"compact-1"** or **"compact-2"**). For these syntaxes, we define under ``"@context"`` a shortcut for the common part of the semantic property names which are formatted as internationalized resource identifiers (IRIs) within the openMINDS schemas. 

How the common part of the semantic property names is shortcutted depends on the compact syntax:

* **compact-1** makes use of the JSON-LD keyword ``"@vocab"`` which can be used to set a common IRI prefix for all properties that do not match a JSON-LD keyword, an IRI, a compact IRI, or blank node identifier (ID). 
* **compact-2** defines a customized short term for the common IRI prefix (here ``"om": "httpXXX"``). In this syntax the property names have to be specified as compact IRIs (here ``"om:givenName"``). 

Both compact syntaxes can be interpreted by any tool that is aware of the JSON-LD specifications. In case no compact syntax is used, the JSON-LD has to be defined with the full semantic property names (cf. **expanded**).

**"@id"**: The JSON-LD keyword ``"@id"`` is used to provide a unique, referable identifier for an instance in a linked metadata collection (cf. `Linking instances`_). In accordance with the JSON-LD specifications, the ``"@id"`` has to be an IRI, a compact IRI or a blank node ID. Which option is chosen is user dependent. However, be aware that within a linked metadata collection each instance has to have a unique ``"@id"``. Our recommendations are as follows: 

- For a local metadata collection the ``"@id"`` of instances can be defined as blank node ID. A blank node ID has the form of ``"_:suffix"``. The suffix can either be a unique human-readable label or a numerical identifier. Be aware that blank node identifier are not persistent or portable. 
- For a portable metadata collection the ``"@id"`` of instances have to be replaced with globally unique and persistent identifiers (e.g., a system-wide IRI prefix in combination with an universially unique identifier (UUID)).

**"@type"**: The JSON-LD keyword ``"@type"`` is used to set the type of an instance or an embedded typed object within an instance. The ``"@type"`` clearly identifies the metadata schema that should be used to validate the content of an instance or an embedded typed object.

Linking instances
#################

Connections between instances of a linked metadata collection are formed by refering to instance's unique identifiers. The "Person" schema tells us that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactinformation>`_ is actually expecting a link (edge) to another instance (object) of type "ContactInformation". Let us create an instance of type "ContactInformation" and link it from a "Person" instance. 

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
          "om": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "om:email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
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
          "om": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "om:contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "om:familyName": "Beeblebrox",
        "om:givenName": "Zaphod"
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

Embedded typed objects
######################

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
          "om": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "om:fullName": "Heart of Gold Spacecraft Crew"
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
          "om": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "om:affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "om:memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "om:contactInformation": {
          "@id": "_:zaphod-beeblebrox_email"
        },
        "om:familyName": "Beeblebrox",
        "om:givenName": "Zaphod"
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

Note that embedded typed objects within an instance do not receive an individual ``"@id"``. In accordance with the JSON-LD specifications, they are inseparable from their parent instance and are not individually referable. 
