###################
openMINDS instances
###################

openMINDS metadata instances should be provided as JSON-LD files and comply to the openMINDS schema type they reference. In the following we will demonstrate how to create an openMINDS metadata instances for a simple example.

Creating minimal Person instance
################################

In order to creat a Person instance we need to check out the constraints defined in the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_.

The schema demands only one required property, namely the property `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#givenname>`_. The schema states also that for the property "givenName" only one value of data type "string" is expected. The property `"familyName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#familyname>`_ is optional, but with the same value constraints as the "givenName"

Based on this information let us define a minimal Person instance:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/person/ZaphodBeeblebrox",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "familyName": "Beeblebrox",
     "givenName": "Zaphod"
   }
