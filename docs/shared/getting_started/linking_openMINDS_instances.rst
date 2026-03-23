##########################################
Linking and embedding openMINDS instances
##########################################

In openMINDS, metadata is structured as interconnected objects.

These objects are either:

- **linked instances**: separate nodes with their own ``"@id"`` that can be referenced from multiple places  
- **embedded typed objects**: nested objects defined within another instance and not independently referable 

Both are defined by separate schemas and are represented differently in openMINDS instances, as shown below.

Linking instances
#################

Some properties in openMINDS schemas expect links to other instances.

For example, the "Person" schema defines the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#contactinformation>`_, which refers to an instance of type "ContactInformation".

A minimal "ContactInformation" instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:zaphod-beeblebrox_email",
     "@type": "https://openminds.om-i.org/types/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

This instance can then be linked from a "Person" instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:zaphod-beeblebrox",
     "@type": "https://openminds.om-i.org/types/Person",
     "contactInformation": {
       "@id": "_:zaphod-beeblebrox_email"
     },
     "givenName": "Zaphod"
   }

The link is written as a JSON object that contains an ``"@id"`` key-value pair referencing the identifier of the target instance.

Embedded typed objects
######################

Some properties expect embedded objects instead of links.

For example, the "Person" schema defines the property `"affiliation" <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html#affiliation>`_, which expects objects of type "Affiliation".

The "Affiliation" schema requires the property ``"memberOf"``, which references an instance of type "Consortium" or "Organization". A minimal "Consortium" instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:heart-of-gold-crew",
     "@type": "https://openminds.om-i.org/types/Consortium",
     "fullName": "Heart of Gold Spacecraft Crew"
   }

The embedded "Affiliation" object is defined directly within the "Person" instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:zaphod-beeblebrox",
     "@type": "https://openminds.om-i.org/types/Person",
     "affiliation": [
       {
         "@type": "https://openminds.om-i.org/types/Affiliation",
         "memberOf": {
           "@id": "_:heart-of-gold-crew"
         }
       }
     ],
     "givenName": "Zaphod"
   }

Embedded objects:

- are typed using ``"@type"``  
- do not have their own ``"@id"``  
- cannot be referenced independently  
- are defined only in the context of their parent instance  

----

By combining linked instances and embedded objects, openMINDS metadata can represent complex data structures.
