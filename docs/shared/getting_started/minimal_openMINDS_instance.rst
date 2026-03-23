############################
A minimal openMINDS instance
############################

openMINDS metadata instances are represented as JSON-LD documents (file extension: ``*.jsonld``) and must comply with the openMINDS schema type they reference.

This page shows how a minimal openMINDS instance is constructed from a schema specification. The JSON-LD elements used here are introduced in the previous page (JSON-LD: minimal introduction).

Creating a minimal instance
###########################

Let us start with a simple "Person" instance, designed according to the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_.

If you inspect the schema, you will see that only the property `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#givenname>`_ is required. The property accepts a single value of type ``"string"``. All other properties are optional.

A minimal openMINDS "Person" instance can therefore look like this:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.om-i.org/types/Person",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "om": "https://openminds.om-i.org/props/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.om-i.org/types/Person",
        "om:givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.om-i.org/types/Person",
        "https://openminds.om-i.org/props/givenName": "Zaphod"
      }

As explained in the previous page, these three representations are equivalent and differ only in how property names are written.

In openMINDS, the **compact-1** syntax using ``"@vocab"`` is typically preferred, as it provides a concise and consistent representation without requiring prefixed property names.

The next step is to connect multiple instances into a linked metadata structure.

----------------------

As shown above, three JSON-LD syntaxes can be used (**"compact-1"**, **"compact-2"**, and **"expanded"**). In the following, we explain these syntaxes together with the meaning of the JSON-LD keywords (``"@context"``, ``"@vocab"``, ``"@id"``, and ``"@type"``).

**"@context"**: The JSON-LD keyword ``"@context"`` must be specified when using one of the compact syntaxes (**"compact-1"** or **"compact-2"**). It defines a shortcut for the common part of semantic property names, which are expressed as internationalized resource identifiers (IRIs) in openMINDS schemas. 

The handling of this common prefix differs between the compact syntaxes:

- **compact-1** uses the JSON-LD keyword ``"@vocab"`` to define a default IRI prefix for all properties that are not JSON-LD keywords, IRIs, compact IRIs, or blank node identifiers.  
- **compact-2** defines a custom prefix (e.g., ``"om": "httpXXX"``). Property names must then be expressed as compact IRIs (e.g., ``"om:givenName"``).  

Both compact syntaxes can be interpreted by any JSON-LD-compliant tool. If no compact syntax is used, full IRIs must be specified (cf. **expanded**).

**"@id"**: The JSON-LD keyword ``"@id"`` provides a unique, referable identifier for an instance within a linked metadata collection (cf. `Linking instances`_). It must be an IRI, a compact IRI, or a blank node identifier.

Within a linked metadata collection, each instance must have a unique ``"@id"``. Recommended usage:

- For local metadata collections, ``"@id"`` values can be defined as blank node identifiers of the form ``"_:suffix"``. The suffix may be a human-readable label or a numerical identifier. Note that blank node identifiers are not persistent or portable.  
- For portable metadata collections, ``"@id"`` values should be globally unique and persistent identifiers (e.g., a system-wide IRI prefix combined with a universally unique identifier (UUID)).

**"@type"**: The JSON-LD keyword ``"@type"`` specifies the type of an instance or an embedded typed object. It identifies the metadata schema used to validate the instance or object.

Linking instances
#################

Connections between instances in a linked metadata collection are established by referencing their unique identifiers. The "Person" schema specifies that the property `"contactInformation" <...>`_ expects a link to an instance of type "ContactInformation".
Connections between instances in a linked metadata collection are established by referencing their unique identifiers. The "Person" schema specifies that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactinformation>`_ expects a link to an instance of type "ContactInformation".

Inspecting the `"ContactInformation" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contactInformation.html>`_ shows that this type requires only the property `"email" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/contactInformation.html#email>`_, which accepts a single string value. A corresponding instance could be defined as follows:

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

We can now extend the previous "Person" instance by adding the optional properties `"familyName" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#familyname>`_ (a string value) and `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactInformation>`_ (a link to a "ContactInformation" instance):

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

Instances can also include embedded typed objects that are constrained by schemas different from that of the parent instance. For example, the "Person" schema specifies that the property `"affiliation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#affiliation>`_ expects one or more embedded objects of type "Affiliation".

Inspecting the `"Affiliation" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html>`_ shows that it requires the property `"memberOf" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/affiliation.html#memberof>`_, which links to an instance of type "Consortium" or "Organization".  

The `"Consortium" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_ and `"Organization" schema <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ schemas both require the property "fullName", defined as a single string value.

To embed an "Affiliation" object in a "Person" instance, at least one "Organization" or "Consortium" instance must first be defined:

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

Note that embedded typed objects do not receive an individual ``"@id"``. According to the JSON-LD specification, they are inseparable from their parent instance and cannot be referenced independently.
