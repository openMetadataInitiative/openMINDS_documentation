##############################
Connecting openMINDS instances
##############################

In openMINDS, metadata is structured as interconnected objects. These objects are either:

- **linked instances**: separate nodes with their own ``"@id"`` that can be referenced from multiple places  
- **embedded typed objects**: nested objects defined within another instance and not independently referable  

Both are defined by separate schemas and are represented differently in openMINDS instances, as shown below.

To demonstrate this, we use the following Organization instance `Organization schema`_, which is gradually extended throughout this page:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:vcf-earth",
     "@type": "https://openminds.om-i.org/types/Organization",
     "name": "Vogon Constructor Fleet, Earth Demolition Subdivision"
   }

Linking instances
#################

Some properties in openMINDS schemas expect links to other instances.

For example, the `Organization schema`_ requires, in addition to the string property ``"name"``, the property `countryOfFormation`_, which refers to an instance of type `SovereignState schema`_.
 
A minimal SovereignState instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:vogonsphere",
     "@type": "https://openminds.om-i.org/types/SovereignState",
     "name": "Vogonsphere"
   }

This instance can then be referenced from the Organization instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:vcf-earth",
     "@type": "https://openminds.om-i.org/types/Organization",
     "countryOfFormation": {
       "@id": "_:vogonsphere"
     },
     "name": "Vogon Constructor Fleet, Earth Demolition Subdivision"
   }

The link is written as a JSON object that contains an ``"@id"`` key-value pair referencing the identifier of the target instance.

Embedded typed objects
######################

Some properties expect embedded objects instead of links.

For example, the Organization schema defines the property ``membership``, which expects an embedded object array with items of type `Membership schema`_.

Although a Membership object is defined by its own schema, its properties are directly provided within the Organization instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:vogon-constructor-fleet-earth-branch",
     "@type": "https://openminds.om-i.org/types/Organization",
     "countryOfFormation": {
       "@id": "_:vogonsphere"
     },
     "membership": [
       {
         "@type": "https://openminds.om-i.org/types/Membership",
         "member": {
           "@id": "_:pv-jeltz"
         },
         "startDate": "1978-04-01"
       }
     ],
     "name": "Vogon Constructor Fleet Earth Branch"
   }

Embedded objects can specify properties with simple string or numeric values, links to independent instances (as here linking to the Person defined in the previous page), or further embedded objects. Moreover, they:

- are typed using ``"@type"``  
- do not have their own ``"@id"``  
- cannot be referenced independently  
- are defined only in the context of their parent instance  

A further point illustrated by this example: if a property expects an array (of simple values, linked instances, or embedded objects) an openMINDS instance always has to provide an array even if only one item is provided.

Linking openMINDS library instances
###################################

For selected schemas, the openMINDS framework provides curated `instance libraries`_. If desired, these globally defined library instances can be linked in the same way as user-defined instances.

For example, the Organization schema requires the property ``type``, which expects a linked instance of type `OrganizationType schema`_.

Instead of defining an individual instance (as we did above for SouvereignState), we use the `openMINDS OrganizationType library`_ and simply reference the desired type (`organizational unit`_) using its openMINDS-defined ``"@id"``:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:vcf-earth",
     "@type": "https://openminds.om-i.org/types/Organization",
     "countryOfFormation": {
       "@id": "_:vogonsphere"
     },
     "membership": [
       {
         "@type": "https://openminds.om-i.org/types/Membership",
         "member": {
           "@id": "_:pv-jeltz"
         },
         "startDate": "1978-04-01"
       }
     ],
     "name": "Vogon Constructor Fleet Earth Branch",
     "type": {
       "@id": "https://openminds.om-i.org/instances/organizationType/organizationalUnit"
     }
   }

The benefit of using instances from the openMINDS library is that they are already defined and used across projects, supporting data harmonisation and integration.

As with other openMINDS-defined IRIs for properties and ``"@type"``, the namespace of these ``"@id"`` values also depends on the openMINDS version:

.. tabs:: instance-id-namespace

   .. code-tab:: text
      :caption: v4.0+

      "https://openminds.om-i.org/instances/SCHEMA-NAME/INSTANCE-NAME"

   .. code-tab:: text
      :caption: ≤ v3.0

      "https://openminds.ebrains.eu/instances/SCHEMA-NAME/INSTANCE-NAME"

Be aware that in an ``"@id"``, the ``SCHEMA-NAME`` is written in lowerCamelCase, in contrast to the UpperCamelCase notation used in ``"@type"``.

The exact ``"@id"`` of a library instance for a given openMINDS version can be found in the corresponding instance library entry.

.. note::

   The Membership, OrganizationType, and SovereignState schemas, as well as the related instance libraries, are only available from openMINDS v5.0 onward. When working with earlier versions, alternative schemas are required to test embedding and linking.

----

By combining linked instances, embedded objects, and optional references to globally provided openMINDS library instances, openMINDS metadata can represent complex graph structures.

The following chapter shows how these interconnected instances are organized into openMINDS metadata collections.

.. _SovereignState schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/controlledTerms/sovereignState.html
.. _Membership schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/membership.html
.. _OrganizationType schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/controlledTerms/organizationType.html

.. _instance libraries: https://openminds.docs.om-i.org/en/latest/instance_libraries.html
.. _openMINDS OrganizationType library: https://openminds.docs.om-i.org/en/latest/instance_libraries/terminologies/organizationType.html
.. _organizational unit: https://openminds.docs.om-i.org/en/latest/instance_libraries/terminologies/organizationType.html#organizationalunit
