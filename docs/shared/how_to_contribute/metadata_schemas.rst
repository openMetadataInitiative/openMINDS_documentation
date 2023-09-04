################
Metadata schemas
################

If you want to contribute to openMINDS by adding a new or modify an existing schema we advise you to first review the openMINDS syntax and read through our development guidelines.

openMINDS syntax
################

The openMINDS metadata schemas are first developed as templates and written in a framework specific syntax and then translated to other commonly known schema formats via the openMINDS pipeline. The file extension of an openMINDS schema template is: ``*.schema.tpl.json``.

**********
Essentials 
**********

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


Development guidelines
######################

#. All items of a schema should be alphabetically ordered.
#. Default language setting is US English.
