##################
ContentTypePattern
##################

:Semantic name: https://openminds.ebrains.eu/core/ContentTypePattern


------------

------------

Properties
##########

:Required: `contentType <contentType_heading_>`_, `regex <regex_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _contentType_heading:

***********
contentType
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentType
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/data/contentType.html>`_
   :instructions: Add the content type that can be defined by the regular expression of this content type pattern (e.g., for file extensions).

`BACK TO TOP <ContentTypePattern_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this content type pattern that may help you to find this instance more easily.

`BACK TO TOP <ContentTypePattern_>`_

------------

.. _regex_heading:

*****
regex
*****

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/regex
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the regular expression for common elements within the file names (including their file path and/or extension) of the files formatted using the stated 'contentType'.

`BACK TO TOP <ContentTypePattern_>`_

------------

