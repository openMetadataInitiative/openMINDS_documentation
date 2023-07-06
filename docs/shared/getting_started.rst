###############
Getting started
###############

This chapter offers an overview of the openMINDS metadata models from a practical perspective. 
Please note that this overview will by no means cover all annotation options the openMINDS metadata models offer.
However, we hope we can provide you with a good starting point to create an openMINDS metadata collection for your data.


******
Basics
******

openMINDS provides schema specifications for metadata models that are tailored for data representations in graph databases.
Information in graph databases is represented in **nodes** that are linked via **edges**. 

openMINDS currently supports the World Wide Web Consortium (W3C) recommendation for `JSON-LD <https://json-ld.org/>`_ \(JavaScript Object Notation for Linked Data\) to encode linked metadata instances.

Let us assume the following simplified openMINDS schema specification for defining a person in JSON-Schema:

.. code-block:: json

   {
     "$id": "https://openminds.ebrains.eu/core/person?format=json-schema",
     "$schema": "http://json-schema.org/draft-07/schema#",
     "properties": {
       "@id": {
         "type": "string"
       },
       "@type": {
         "type": "string"
       },
       "https://openminds.ebrains.eu/vocab/familyName": {
         "type": "string"
       },
       "https://openminds.ebrains.eu/vocab/givenName": {
         "type": "string"
       }
     },
     "required": [
       "@id",
       "@type",
       "https://openminds.ebrains.eu/vocab/givenName"
     ],
     "type": "object"
   }

The respectively correct serialization of this schema in JSON-LD would be the following:

.. example-code::

.. code-block:: json

   {
     "@id": "https://localhost/person_zehl_lyuba.jsonld",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "https://openminds.ebrains.eu/vocab/familyName": "Zehl",
     "https://openminds.ebrains.eu/vocab/givenName": "Lyuba"
   }

.. code-block:: json

   {
     "@context": {
       "@vocab": "https://openminds.ebrains.eu/vocab/"
     },
     "@id": "https://localhost/person_zehl_lyuba.jsonld",
     "@type": "https://openminds.ebrains.eu/core/Person",
     "familyName": "Zehl",
     "givenName": "Lyuba"
   }

*****************
Research products
*****************

The openMINDS metadata models are centered around research products:

| - **Dataset** (focus: data originating from human, animal or simulation experiment)
| - **Model** (focus: data and code defining a computational model)
| - **Software** (focus: data and code defining a software tool)
| - **MetaDataModel** (focus: data defining specifications of a data or metadata model)
| - **BrainAtlas** (focus: data defining a brain atlas)
| - **CommonCoordinatSpace** (focus: data defining a common coordinate space)
| - **LivePaper** (focus: data defining a live paper)
| - **WorkflowRecipe** (focus: data and code defining the recipe of a computational workflow)
| - **WebService** (focus: data and code defining a web service)

.. note:: Note
   Please be aware that early openMINDS versions (\≤ v2.0) only support a reduced list of research products.

*****************
File Repositories
*****************

All research products can link 


.. toctree::
   getting_started/matlab
   getting_started/python
