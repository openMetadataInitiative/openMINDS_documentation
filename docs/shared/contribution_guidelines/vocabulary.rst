##########
Vocabulary
##########

If you want to contribute to openMINDS by adding information to the openMINDS vocabulary we advise you to first review this chapter.

For each contribution, please raise an `ISSUE <https://github.com/openMetadataInitiative/openMINDS/issues>`_. Start the issue title with ``vocab: `` followed by an informative short title for your contribution. Please provide a more detailed explanation of your contribution in issue description. We will discuss your contribution with you before a pull request is made (by you or by us if you do not feel comfortable making a pull request yourself).


Schema types
############

In openMINDS, schema types are considered version independent, meaning the general information about a schema type remains the same across versions (e.g. its description). We maintain this schema type information centrally on the main openMINDS GitHub repository under: `vocab/types.json <https://github.com/openMetadataInitiative/openMINDS/blob/main/vocab/types.json>`_

This file is a simple JSON, where each vocabulary implementation for a single schema type is structured in the following way:

.. code-block:: json

   {
     "SCHEMATYPE": {
       "color": "HEXCOLOR",
       "description": "SCHEMATYPE_DESCRIPTION",
       "isPartOfVersion": [
         "VERSION"
       ],
       "label": "SCHEMALABEL",
       "name": "SCHEMANAME",
       "semanticEquivalent": [
         "UNIQUEID_OF_EQUIVALENT_SCHEMA"
       ]
     }
   }

.. note::

   This file is auto-generated with each new schema commit on openMINDS. However, the attributes ``"color"``, ``"description"``, ``"label"``, and ``"semanticEquivalent"`` can be manually overwritten.

Properties
##########

In openMINDS, general information on properties (e.g., description) are considered schema and (mostly) version independent. We maintain these properties information centrally on the main openMINDS GitHub repository under: `vocab/properties.json <https://github.com/openMetadataInitiative/openMINDS/blob/main/vocab/properties.json>`_

This file is a simple JSON, where each vocabulary implementation for a single property is structured in the following way:

.. code-block:: json

   {
     "PROPERTYNAME": {
       "asString": {
         "formatting": "STRINGFORMAT",
         "inVersions": [
           "VERSION"
         ],
         "multiline": "BOOLEAN"
       },
       "description": "PROPERTYNAME_DESCRIPTION",
       "label": "PROPERTYLABEL",
       "labelPlural": "PROPERTYLABEL",
       "name": "PROPERTYNAME_SHORT",
       "namePlural": "PROPERTYLABEL",
       "semanticEquivalent": [
         "UNIQUEID_OF_EQUIVALENT_PROPERTY"
       ],
       "usedIn": {
         "VERSION": [
           "SCHEMATYPE"
         ]
       }
     }
   }

.. note::

   This file is auto-generated with each new commit on openMINDS. However, the attributes ``"description"``, ``"label"``, ``"labelPlural"``, ``"namePlural"``, and ``"semanticEquivalent"`` can be manually overwritten.
