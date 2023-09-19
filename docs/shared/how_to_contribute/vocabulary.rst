##########
Vocabulary
##########

If you want to contribute to openMINDS by adding information to the openMINDS vocabulary we advise you to first review this chapter.

Schema types
############

The following code block sketches the vocabulary implementation for a single schema type:

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

Properties
##########

The following code block sketches the vocabulary implementation for a single property:

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
       "name": "PROPERTYNAME_SHORT",
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
