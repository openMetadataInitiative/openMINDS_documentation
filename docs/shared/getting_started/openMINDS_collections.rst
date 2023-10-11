#####################
openMINDS collections
#####################

An openMINDS metadata collection is composed of multiple linked instances. The instances of such a collection can either be stored in separate JSON-LD files in a dedicated directory or all together within one collection JSON-LD file. 

In `"openMINDS instances" schema <openMINDS_instances.html>`_ we started a minimal collection which included a "Person" instance linked to a "ContactInformation" instance and with an embedded "Affiliation" that links to a "Consortium" instance. Let us further extend this collection by adding more "Person" instances that are affiliated to the same "Consortium" instance:

.. tabs::

   .. code-tab:: json
      :caption: _:zaphod-beeblebrox (Person)

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
      :caption: _:zaphod-beeblebrox_email (ContactInformation)

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:zaphod-beeblebrox_email",
        "@type": "https://openminds.ebrains.eu/core/ContactInformation",
        "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
      }

   .. code-tab:: json
      :caption: _:heart-of-gold-crew (Consortium)

      {
        "@context": {
          "@vocab": "https://openminds.ebrains.eu/vocab/"
        },
        "@id": "_:heart-of-gold-crew",
        "@type": "https://openminds.ebrains.eu/core/Consortium",
        "fullName": "Heart of Gold Spacecraft Crew"
      }

   .. code-tab:: json
      :caption: _:zaphod-beeblebrox (Person)

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
        "familyName": "Beeblebrox",
        "givenName": "Zaphod"
      }

Dedicated directory
###################

In `"openMINDS instances" schema <openMINDS_instances.html>`_ 
