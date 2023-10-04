###############
FilePathPattern
###############

:Semantic name: https://openminds.ebrains.eu/core/FilePathPattern


------------

------------

Properties
##########

:Required: `groupingType <groupingType_heading_>`_, `regex <regex_heading_>`_
:Optional:

------------

.. _groupingType_heading:

************
groupingType
************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupingType
   :value type: | linked object array \(1-N\) of type
                | `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/controlledTerms/fileBundleGrouping.html>`_
   :instructions: Add all grouping types that are defined by this file path pattern.

`BACK TO TOP <FilePathPattern_>`_

------------

.. _regex_heading:

*****
regex
*****

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/regex
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the regular expression that defines this file path pattern. Note that it must have the same number of groups as stated under 'groupingType'.

`BACK TO TOP <FilePathPattern_>`_

------------

