###########
ContentType
###########

:Semantic name: https://openminds.ebrains.eu/core/ContentType

Structured information on the content type of a file instance, bundle or repository.


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v1.0/instance_libraries/contentTypes.html>`_.

------------

------------

Properties
##########

:Required: `associatedFileExtension <associatedFileExtension_heading_>`_, `category <category_heading_>`_, `name <name_heading_>`_
:Optional: `relatedMediaType <relatedMediaType_heading_>`_, `synonym <synonym_heading_>`_

------------

.. _associatedFileExtension_heading:

***********************
associatedFileExtension
***********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/associatedFileExtension
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter one or several file extensions associated with this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _category_heading:

********
category
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/category
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the category to which this content type belongs to.

`BACK TO TOP <ContentType_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name (iana-inspired convention) of this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _relatedMediaType_heading:

****************
relatedMediaType
****************

Reference to an official two-part identifier for file formats and format contents.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedMediaType
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the iternationalized resource identifier (IRI) to a registered media type (e.g. on IANA.org) matching this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _synonym_heading:

*******
synonym
*******

Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/synonym
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter one or several synonyms of this content type.

`BACK TO TOP <ContentType_>`_

------------

