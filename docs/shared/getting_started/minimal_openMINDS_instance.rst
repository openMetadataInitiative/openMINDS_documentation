############################
A minimal openMINDS instance
############################

openMINDS metadata instances are represented as JSON-LD documents (file extension: ``*.jsonld``) and must comply with the openMINDS schema type they reference.

This page shows how a minimal openMINDS instance is constructed from a schema specification. The JSON-LD elements used here are introduced in the `previous chapter`_.

Creating a minimal instance
###########################

Let us start with a simple "Person" instance, designed according to the `Person schema`_.

If you inspect the schema, you will see that only the property `givenName`_ is required. The property accepts a single value of type ``"string"``. All other properties are optional.

A minimal "Person" instance can therefore look like this:

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

As explained in the previous page, these representations are equivalent and differ only in how property names are written.

In openMINDS, the **compact-1** syntax using ``"@vocab"`` is typically preferred, as it provides a concise and consistent representation without requiring prefixed property names.

openMINDS namespaces
####################

The IRIs used in ``"@type"`` and in the property namespace depend on the openMINDS version.

.. tabs:: namespace-version

   .. code-tab:: json
      :caption: v4.0+

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.om-i.org/types/Person",
        "givenName": "Zaphod"
      }

   .. code-tab:: json
      :caption: ≤ v3.0

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "givenName": "Zaphod"
      }

The following chapters show how openMINDS instances are connected into a linked metadata structure.

.. _previous chapter: jsonld_introduction.html
.. _Person schema: https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html
.. _givenName: https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#givenname
