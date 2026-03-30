###################################
openMINDS metadata collections
###################################

openMINDS instances are typically not used in isolation but combined into collections of interconnected metadata.

Building on the structures introduced in the previous chapter, the current instances (Person, ContactInformation, and Location) form only partially connected components. To form a coherent metadata graph, these components need to be linked through additional instances.

To establish such connections, we introduce an Organization instance that links to the existing Person and Location instances. This creates a fully connected metadata graph that can be organized as an openMINDS metadata collection.

Storing collections
###################

openMINDS metadata collections can be stored in two main ways:

- as multiple JSON-LD files (one instance per file) organized in a directory  
- as a single JSON-LD file containing all instances in a graph structure  

---

Collection directory
####################

In a directory-based collection, each instance is stored in a separate JSON-LD file.

Example instances:

.. tabs:: collection-files

   .. code-tab:: json
      :caption: pv-jeltz.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:pv-jeltz",
        "@type": "https://openminds.om-i.org/types/Person",
        "contactInformation": {
          "@id": "_:pv-jeltz_email"
        },
        "preferredName": "Prostetnic Vogon Jeltz"
      }

   .. code-tab:: json
      :caption: pv-jeltz_email.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:pv-jeltz_email",
        "@type": "https://openminds.om-i.org/types/ContactInformation",
        "email": "pv.jeltz@planning.vogon-constructor-fleet.gal"
      }

   .. code-tab:: json
      :caption: cottington-location.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:cottington-location",
        "@type": "https://openminds.om-i.org/types/Location",
        "address": "Vogon Planning Annex 12-B (Earth Liaison Office), Bypass Way, Cottington Fields, West Country Sector, UK, Earth",
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

These files can be organized in different ways:

.. tabs:: collection-directory

   .. code-tab:: text
      :caption: flat

      myCollection
      |-- pv-jeltz.jsonld
      |-- pv-jeltz_email.jsonld
      `-- cottington-location.jsonld

   .. code-tab:: text
      :caption: grouped by schema

      myCollection
      |-- persons
      |   `-- pv-jeltz.jsonld
      |-- contactInformations
      |   `-- pv-jeltz_email.jsonld
      `-- locations
          `-- cottington-location.jsonld

The organization of files within the directory is flexible. Instances can be stored in a flat structure or grouped by schema type.

---

Collection file
###############

Alternatively, all instances of a collection can be stored in a single JSON-LD file using the ``"@graph"`` keyword.

The ``"@graph"`` keyword defines a list of instances that together form the metadata graph. In this case, the ``"@context"`` can be defined once for all instances:

.. code-block:: json
   :caption: myCollection.jsonld

   {
     "@context": {
       "@vocab": "https://openminds.om-i.org/props/"
     },
     "@graph": [
       {
         "@id": "_:pv-jeltz",
         "@type": "https://openminds.om-i.org/types/Person",
         "contactInformation": {
           "@id": "_:pv-jeltz_email"
         },
         "preferredName": "Prostetnic Vogon Jeltz"
       },
       {
         "@id": "_:pv-jeltz_email",
         "@type": "https://openminds.om-i.org/types/ContactInformation",
         "email": "pv.jeltz@planning.vogon-constructor-fleet.gal"
       },
       {
         "@id": "_:cottington-location",
         "@type": "https://openminds.om-i.org/types/Location",
         "address": "Vogon Planning Annex 12-B (Earth Liaison Office), Bypass Way, Cottington Fields, West Country Sector, UK, Earth",
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
     ]
   }

Both approaches represent the same underlying metadata graph and can be used depending on workflow and tooling.
