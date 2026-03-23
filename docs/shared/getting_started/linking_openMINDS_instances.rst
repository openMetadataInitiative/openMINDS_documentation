##########################################
Linking and embedding openMINDS instances
##########################################

In openMINDS, metadata is represented as a collection of interconnected instances. Connections between instances are formed by referring to their unique identifiers.

Linking instances
#################

Some properties in openMINDS schemas expect links to other instances.

For example, the "Person" schema defines the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactinformation>`_, which refers to an instance of type "ContactInformation".

A minimal "ContactInformation" instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "_:zaphod-beeblebrox_email",
     "@type": "https://openminds.ebrains.eu/core/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

This instance can then be linked from a "Person" instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "_:zaphod-beeblebrox",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "contactInformation": {
       "@id": "_:zaphod-beeblebrox_email"
     },
     "givenName": "Zaphod"
   }

The link is established via the ``"@id"`` of the referenced instance.

Embedded typed objects
######################

Some properties expect embedded objects instead of links.

For example, the "Person" schema defines the property `"affiliation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#affiliation>`_, which expects objects of type "Affiliation".

An embedded object is included directly within the parent instance:

.. code-block:: json

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
     "givenName": "Zaphod"
   }

Embedded objects:

- do not have their own ``"@id"``  
- cannot be referenced independently  
- are only defined in the context of their parent instance  

By combining linked instances and embedded objects, openMINDS metadata can represent complex data structures.
