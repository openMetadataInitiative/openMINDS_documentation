################
Metadata schemas
################

If you want to contribute to openMINDS by adding a new or modify an existing schema we advise you to first review the openMINDS syntax and read through our development guidelines.

openMINDS syntax
################

The openMINDS metadata schemas are first developed as templates and then automatically interpreted and extended with the centrally maintained openMINDS vocabulary to complete metadata schemas through the openMINDS pipeline. Both schema templates (``*.schema.tpl.json``) and complete schemas (``*.schema.omi.json``) are written in an openMINDS-specific syntax. This syntax is loosely based on JSON-Schema, but tailored to facilitate implementation, readability, and maintainability. The openMINDS syntax for templates, vocabulary and complete schemas is explained in the following.

**********
Essentials 
**********
The following code block sketches the most simple implementation of an openMINDS schema template.

.. code-block:: json

   {
     "_type": "SCHEMATYPE",
     "properties": {
       "PROPERTYNAME": {
         "type": "VALUETYPE",
         "_instruction": "INSTRUCTION"
       }
     },
     "required": [
       "PROPERTYNAME"
     ]
   }

Such an openMINDS schema template should be combined with centrally maintained vocabulary for schema types and properties. The following code block sketches the vocabulary implementation for a single schema type:

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

The next code block sketches the vocabulary implementation for a single property:

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

Development guidelines
######################

#. All items of a schema should be alphabetically ordered.
#. Default language setting is US English.
#. A schema should specify a set of properties that meaningfully represents a recurrent type of real-world entities.
#. A schema should not directly specify nested schema definitions (cf. linked and embedded schemas).
#. A schema should be linked, not embedded, if the respective real-world entity can sustain on its own or if it should be individually protected.
#. A schema of a real-world entity that only exists in context of another real-world entity (and therefore “shares its lifecycle”) should be embedded, not linked.
#. A state-varying real world entity should be represented in two interlinked schemas, one for the state-independent and one for the state-dependent information.
#. Within a schema, only properties that can be expected for all respected real-world entities should be made required.
#. If properties of a real-world entity contains potentially sensitive information (e.g., personal data), these properties should be specified in a separate schema.
#. Schema properties should be consistently reduced to a minimum, meaning the reuse of a property name across schemas is highly recommended, if the definition of that property name remains the same.
