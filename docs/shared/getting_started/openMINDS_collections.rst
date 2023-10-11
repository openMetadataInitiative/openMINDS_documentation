#####################
openMINDS collections
#####################

An openMINDS metadata collection is composed of multiple linked instances. The instances of such a collection can either be stored in separate JSON-LD files in a dedicated directory or all together within one collection JSON-LD file. 

In `"openMINDS instances" schema <openMINDS_instances.html>`_ we started a minimal collection which included a "Person" instance linked to a "ContactInformation" instance and with an embedded "Affiliation" that links to a "Consortium" instance. In the following we extended this initial collection by adding three more "Person" instances that are affiliated to the same "Consortium" instance.

Collection directory
####################

The instances of the above stated collection could be stored in separate files:

.. tabs::

   .. code-tab:: json
      :caption: arthur-dent.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:arthur-dent",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "familyName": "Dent",
        "givenName": "Arthur"
      }

   .. code-tab:: json
      :caption: ford-prefect.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:ford-prefect",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "familyName": "Prefect",
        "givenName": "Ford"
      }

   .. code-tab:: json
      :caption: heart-of-gold-crew.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "fullName": "Heart of Gold Spacecraft Crew"
      }

   .. code-tab:: json
      :caption: tricia-marie-mcmillan.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:tricia-marie-mcmillan",
        "@type": "https://openminds.ebrains.eu/core/Person",
        "alternateName": [
          "Trillian Astra"
        ],
        "affiliation": [
          {
            "@type": "https://openminds.ebrains.eu/core/Affiliation",
            "memberOf": {
              "@id": "_:heart-of-gold-crew"
            }
          }
        ],
        "familyName": "McMillan",
        "givenName": "Tricia Marie"
      }

   .. code-tab:: json
      :caption: zaphod-beeblebrox.jsonld

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
      :caption: zaphod-beeblebrox_email.jsonld

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
      }

These separate files should be stored in a dedicated collection directory. The organization of files within such a directory is flexible. In our example we present the files as a flat list (**v1**) or grouped into subdirectories for each type (**v2**):

.. tabs:: collection-directory

   .. code-tab:: markdown
      :caption: v1

      myCollection
      |-- arthur-dent.jsonld
      |-- ford-prefect.jsonld
      |-- heart-of-gold-crew.jsonld
      |-- tricia-marie-mcmillan.jsonld
      |-- zaphod-beeblebrox.jsonld
      `-- zaphod-beeblebrox_email.jsonld

   .. code-tab:: markdown
      :caption: v2

      myCollection
      |-- consortia
      |   `-- heart-of-gold-crew.jsonld
      |-- contactInformations
      |   `-- zaphod-beeblebrox_email.jsonld
      `-- persons
          |-- arthur-dent.jsonld
          |-- ford-prefect.jsonld
          |-- tricia-marie-mcmillan.jsonld
          `-- zaphod-beeblebrox.jsonld

If the collection contains instances that contain sensitive information, these instances can be stored in a protected subdirectory. For our example directories above that could look like this:

.. tabs:: collection-directory

   .. code-tab:: markdown
      :caption: v1

      myCollection
      |-- private
      |   `-- zaphod-beeblebrox_email.jsonld
      `-- public
          |-- arthur-dent.jsonld
          |-- ford-prefect.jsonld
          |-- heart-of-gold-crew.jsonld
          |-- tricia-marie-mcmillan.jsonld
          `-- zaphod-beeblebrox.jsonld


   .. code-tab:: markdown
      :caption: v2

      myCollection
      |-- private
      |   `-- contactInformations
      |       `-- zaphod-beeblebrox_email.jsonld
      `-- public
          |-- consortia
          |   `-- heart-of-gold-crew.jsonld
          `-- persons
              |-- arthur-dent.jsonld
              |-- ford-prefect.jsonld
              |-- tricia-marie-mcmillan.jsonld
              `-- zaphod-beeblebrox.jsonld

Collection file
###############

It is also possible to store all instances of an openMINDS metadata collection into a single JSON-LD file in form of a simple graph object. In such a case the JSON-LD keyword ``"@context"`` can be globally defined for all instances listed under the JSON-LD keyword ``"@graph"``:

.. code-block:: json
   :caption: myCollection.jsonld

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@graph": [
       {
         "@id": "_:arthur-dent",
         "@type": "https://openminds.ebrains.eu/core/Person",
         "affiliation": [
           {
             "@type": "https://openminds.ebrains.eu/core/Affiliation",
             "memberOf": {
               "@id": "_:heart-of-gold-crew"
             }
           }
         ],
         "familyName": "Dent",
         "givenName": "Arthur"
       },
       {
         "@id": "_:ford-prefect",
         "@type": "https://openminds.ebrains.eu/core/Person",
         "affiliation": [
           {
             "@type": "https://openminds.ebrains.eu/core/Affiliation",
             "memberOf": {
               "@id": "_:heart-of-gold-crew"
             }
           }
         ],
         "familyName": "Prefect",
         "givenName": "Ford"
       },
       {
         "@id": "_:heart-of-gold-crew",
         "@type": "https://openminds.ebrains.eu/core/Consortium",
         "fullName": "Heart of Gold Spacecraft Crew"
       },
       {
         "@id": "_:tricia-marie-mcmillan",
         "@type": "https://openminds.ebrains.eu/core/Person",
         "alternateName": [
           "Trillian Astra"
         ],
         "affiliation": [
           {
             "@type": "https://openminds.ebrains.eu/core/Affiliation",
             "memberOf": {
               "@id": "_:heart-of-gold-crew"
             }
           }
         ],
         "familyName": "McMillan",
         "givenName": "Tricia Marie"
       },
       {
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
       },
       {
         "@id": "_:zaphod-beeblebrox_email",
         "@type": "https://openminds.ebrains.eu/core/ContactInformation",
         "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
       }
     ]
   }
