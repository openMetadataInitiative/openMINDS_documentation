##############################
Connecting openMINDS instances
##############################

In openMINDS, metadata is structured as interconnected objects.

These objects are either:

- **linked instances**: separate nodes with their own ``"@id"`` that can be referenced from multiple places  
- **embedded typed objects**: nested objects defined within another instance and not independently referable  

Both are defined by separate schemas and are represented differently in openMINDS instances, as shown below.

Linking instances
#################

Some properties in openMINDS schemas expect links to other instances.

For example, the `Person schema`_ defines the property `contactInformation`_, which refers to an instance of type `ContactInformation schema`_.

A minimal ContactInformation instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:zaphod-beeblebrox_email",
     "@type": "https://openminds.om-i.org/types/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

This instance can then be referenced from a Person instance:

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
     "preferredName": "Zaphod Beeblebrox"
   }

The link is written as a JSON object that contains an ``"@id"`` key-value pair referencing the identifier of the target instance.

Embedded typed objects
######################

Some properties expect embedded objects instead of links.

For example, the `Location schema`_ defines, besides the required simple string property `address`_, an optional embedded object property `geoCoordinates`_.

Although the structure of the embedded object is specified by the `GeoCoordinates schema`_, its definition is provided directly within the Location instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@id": "_:cottington-location",
     "@type": "https://openminds.om-i.org/types/Location",
     "address": "42B Bypass Way, Cottington Fields, West Country Sector, UK, Earth",
     "geoCoordinates": {
       "@type": "https://openminds.om-i.org/types/GeoCoordinates",
       "elevation": 128.0,
       "latitude": 51.8437,
       "longitude": -2.9213
     }
   }

Embedded objects:

- are typed using ``"@type"``  
- do not have their own ``"@id"``  
- cannot be referenced independently  
- are defined only in the context of their parent instance  

Linking openMINDS library instances
###################################

For selected schemas, the openMINDS framework provides curated `instance libraries`_.

If desired, these globally defined library instances can be linked in the same way as user-defined instances.

For example, the Location schema requires, besides ``"address"``, also the property `country`_, which expects a linked instance of type `SovereignState schema`_.

Instead of defining an individual instance, the desired country (`United Kingdom`_) can be referenced directly from the `openMINDS SovereignState library`_:

.. tabs:: library-instance-version

   .. code-tab:: json
      :caption: v4.0+

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:cottington-location",
        "@type": "https://openminds.om-i.org/types/Location",
        "address": "42B Bypass Way, Cottington Fields, West Country Sector, UK, Earth",
        "geoCoordinates": {
          "@type": "https://openminds.om-i.org/types/GeoCoordinates",
          "elevation": 128.0,
          "latitude": 51.8437,
          "longitude": -2.9213
        },
        "country": {
          "@id": "https://openminds.om-i.org/instances/sovereignStates/UnitedKingdom"
        }
      }

   .. code-tab:: json
      :caption: ≤ v3.0

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:cottington-location",
        "@type": "https://openminds.ebrains.eu/core/Location",
        "address": "42B Bypass Way, Cottington Fields, West Country Sector, UK, Earth",
        "geoCoordinates": {
          "@type": "https://openminds.ebrains.eu/core/GeoCoordinates",
          "elevation": 128.0,
          "latitude": 51.8437,
          "longitude": -2.9213
        },
        "country": {
          "@id": "https://openminds.ebrains.eu/instances/sovereignStates/UnitedKingdom"
        }
      }


Library instances are referenced via their openMINDS-defined ``"@id"``, which are unique IRIs. Namespace differences between openMINDS versions therefore also affect the ``"@id"`` values used when linking library instances.

.. note::

   The Location, GeoCoordinates, and SovereignState schemas, as well as the related SovereignState instance library, are only available from openMINDS v5.0 onward. When working with earlier versions, alternative schemas are required to test embedding and linking.

----

By combining linked instances, embedded objects, and optional references to globally provided openMINDS library instances, openMINDS metadata can represent complex graph structures while supporting interoperability and integration across Linked Data.

.. _Person schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/actors/person.html
.. _contactInformation: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/actors/person.html#contactinformation
.. _ContactInformation schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/actors/contactInformation.html

.. _Location schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/location.html
.. _address: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/location.html#address
.. _geoCoordinates: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/location.html#geocoordinates
.. _GeoCoordinates schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/geoCoordinates.html
.. _country: https://openminds.docs.om-i.org/en/latest/schema_specifications/core/miscellaneous/location.html#country

.. _instance libraries: https://openminds.docs.om-i.org/en/latest/instance_libraries.html
.. _openMINDS SovereignState library: https://openminds.docs.om-i.org/en/latest/instance_libraries/terminologies/sovereignState.html#
.. _United Kingdom: https://openminds.docs.om-i.org/en/latest/instance_libraries/terminologies/sovereignState.html#unitedkingdom
.. _SovereignState schema: https://openminds.docs.om-i.org/en/latest/schema_specifications/controlledTerms/sovereignState.html
