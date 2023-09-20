###################
openMINDS instances
###################

openMINDS instances should be provided as JSON-LD files (``*.jsonld``) and comply to the openMINDS schema type they reference. In the following we will demonstrate how to create openMINDS instances for simple examples.

Creating a minimal instance
###########################

Let us start be creating a "Person" instance. For this, we first need to check the constraints defined in the `"Person" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_.

The "Person" schema demands only one required property, named `"givenName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#givenname>`_. The schema states also that for the property "givenName" only a single value of data type "string" is expected. The remaining properties of the schema are optional and do not have to be specified in a valid openMINDS "Person" instance. 

Nonetheless, for our example, let us also specify the optional property `"familyName" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#familyname>`_ which has the same value constraints as the "givenName". Based on these constraints, let us define a minimal "Person" instance:

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

Link an instance with another instance
######################################

Let us now link the minimal "Person" instance we've created with metadata defined in an other instance. The "Person" schema tells us that the property `"contactInformation" <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html#contactinformation>`_ is actually an edge that should link to an instance of type "ContactInformation". We will therefore have to create a second instance of type "ContactInformation".

If we ckeck the constraints of the `"ContactInformation" schema <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contactInformation.html>`_, we learn that an instance of this type only requires the property "email" defined through a single value of data type "string". A respective "ContactInformation" instance could look like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/contactInformation/ZaphodBeeblebrox",
     "@type": "https://openminds.ebrains.eu/core/ContactInformation",
     "email": "zaphod-beeblebrox@hitchhikers-guide.galaxy"
   }

And we can link this "ContactInformation" instance in our "Person" instance like this:

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "http://localhost/openminds/instance/person/ZaphodBeeblebrox",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "contactInformation": {
       "@id": "http://localhost/openminds/instance/contactInformation/ZaphodBeeblebrox"
     },
     "familyName": "Beeblebrox",
     "givenName": "Zaphod"
   }
