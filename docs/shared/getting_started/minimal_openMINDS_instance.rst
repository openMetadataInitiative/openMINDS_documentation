############################
A minimal openMINDS instance
############################

openMINDS metadata instances are represented as JSON-LD documents (file extension: ``*.jsonld``) and must comply with the openMINDS schema type they reference.

This page shows how a minimal openMINDS instance is constructed from a schema specification. The JSON-LD elements used here are introduced in the `previous chapter`_.

Creating a minimal instance
###########################

Let us start with a simple Person instance, designed according to the `Person`_ schema.

If you inspect the schema, you will see that only the property `preferredName`_ is required. The property accepts a single value of type ``"string"``. All other properties are optional.

A minimal Person instance can therefore look like this:

.. tabs:: instance-formatting

   .. code-tab:: json
      :caption: compact-1

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:pv-jeltz",
        "@type": "https://openminds.om-i.org/types/Person",
        "preferredName": "Prostetnic Vogon Jeltz"
      }

   .. code-tab:: json
      :caption: compact-2

      {
        "@context": {
          "om": "https://openminds.om-i.org/props/"
        },
        "@id": "_:pv-jeltz",
        "@type": "https://openminds.om-i.org/types/Person",
        "om:preferredName": "Prostetnic Vogon Jeltz"
      }

   .. code-tab:: json
      :caption: expanded

      {
        "@id": "_:pv-jeltz",
        "@type": "https://openminds.om-i.org/types/Person",
        "https://openminds.om-i.org/props/preferredName": "Prostetnic Vogon Jeltz"
      }

As explained in the previous page, the instance representations **compact-1**, **compact-2**, and **expanded** are equivalent and differ only in how property names are written.

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
        "@id": "INSTANCE-IDENTIFIER",
        "@type": "https://openminds.om-i.org/types/SCHEMA-NAME",
        "PROPERTY-NAME": "PROPERTY-VALUE"
      }

   .. code-tab:: json
      :caption: ≤ v3.0

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "INSTANCE-IDENTIFIER",
        "@type": "https://openminds.ebrains.eu/MODULE-NAME/SCHEMA-NAME",
        "PROPERTY-NAME": "PROPERTY-VALUE"
      }

The applicable namespace pattern can be found in the corresponding schema specification for the openMINDS version you are using.

.. note::

   In openMINDS v3.0 and earlier, schema type IRIs include ``MODULE-NAME`` as an additional path component. While modularization continues to be used for maintenance and schema dependency logic, it is no longer reflected in the namespace to simplify IRIs.

----

The following chapter shows how individual openMINDS instances are connected and structured into a graph.

.. _previous chapter: jsonld_introduction.html
.. _Person: https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html
.. _preferredName: https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#preferredname
