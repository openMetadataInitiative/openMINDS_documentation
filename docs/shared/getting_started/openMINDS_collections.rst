##############################
openMINDS metadata collections
##############################

openMINDS instances are typically not used in isolation but combined into collections of interconnected metadata.

In the previous chapter, we connected the following instances into a coherent metadata graph:

.. tabs:: collection-files

   .. code-tab:: json
      :caption: Person

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:pv-jeltz",
        "@type": "https://openminds.om-i.org/types/Person",
        "preferredName": "Prostetnic Vogon Jeltz"
      }

   .. code-tab:: json
      :caption: Organization

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
        "name": "Vogon Constructor Fleet, Earth Demolition Subdivision",
        "type": {
          "@id": "https://openminds.om-i.org/instances/organizationType/organizationalUnit"
        }
      }

   .. code-tab:: json
      :caption: SovereignState

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "_:vogonsphere",
        "@type": "https://openminds.om-i.org/types/SovereignState",
        "name": "Vogonsphere"
      }

   .. code-tab:: json
      :caption: OrganizationType

      {
        "@context": {
          "@vocab": "https://openminds.om-i.org/props/"
        },
        "@id": "https://openminds.om-i.org/instances/organizationType/organizationalUnit",
        "@type": "https://openminds.om-i.org/types/OrganizationType",
        "definition": "A distinct unit within a larger organization.",
        "name": "organizational unit"
      }

A Person (Prostetnic Vogon Jeltz) who is a member of an Organization (Vogon Constructor Fleet, Earth Demolition Subdivision) which specifies its country of formation in a custom-defined SovereignState (Vogonsphere) and its OrganizationType (organizational unit) from an openMINDS instance library.

For a metadata collection to be complete and fully valid, all referenced instances must be included in the collection. This also applies to instances originating from openMINDS instance libraries.

Storing collections
###################

openMINDS metadata collections can be stored in two main ways:

- as multiple JSON-LD files organized in a directory  
- as a single JSON-LD file containing all instances in one graph structure  

Collection directory
####################

In a directory-based collection, each instance is stored in a separate JSON-LD file.

These files can be in a flat structure or grouped by schema type:

.. tabs:: collection-directory

   .. code-tab:: text
      :caption: flat

      myCollection
      |-- pv-jeltz.jsonld
      |-- vcf-earth.jsonld
      |-- vogonsphere.jsonld
      `-- organizational-unit.jsonld

   .. code-tab:: text
      :caption: grouped by schema

      myCollection
      |-- persons
      |   `-- pv-jeltz.jsonld
      |-- organizations
      |   `-- vcf-earth.jsonld
      |-- organizationTypes
      |   `-- organizational-unit.jsonld
      |-- sovereignStates
          `-- vogonsphere.jsonld

Collection file
###############

Alternatively, all instances of a collection can be stored in a single JSON-LD file.

In this case, the JSON-LD keyword ``"@graph"`` is used to define a list of objects that together form the metadata graph.

Unlike a directory-based collection, where each file defines its own ``"@context"``, a collection file can define one common ``"@context"`` at the top level. This context then applies to all objects listed under ``"@graph"``.

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
         "preferredName": "Prostetnic Vogon Jeltz"
       },
       {
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
         "name": "Vogon Constructor Fleet, Earth Demolition Subdivision",
         "type": {
           "@id": "https://openminds.om-i.org/instances/organizationType/organizationalUnit"
         }
       },
       {
         "@id": "_:vogonsphere",
         "@type": "https://openminds.om-i.org/types/SovereignState",
         "name": "Vogonsphere"
       },
       {
         "@id": "https://openminds.om-i.org/instances/organizationType/organizationalUnit",
         "@type": "https://openminds.om-i.org/types/OrganizationType",
         "definition": "A distinct unit within a larger organization.",
         "name": "organizational unit"
       }
     ]
   }

Both approaches represent the same underlying metadata graph and can be used depending on workflow and tooling.
