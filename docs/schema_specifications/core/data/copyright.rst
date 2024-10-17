#########
Copyright
#########

:Semantic name: core:Copyright

:Display as: Core:copyright


------------

------------

Properties
##########

:Required: `holder <holder_heading_>`_, `year <year_heading_>`_
:Optional:

------------

.. _holder_heading:

******
holder
******

Legal person in possession of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/holder
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that hold this copyright.

`BACK TO TOP <Copyright_>`_

------------

.. _year_heading:

****
year
****

Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/year
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the year during which the copyright was first asserted and, optionally, later years during which updated versions were published.

`BACK TO TOP <Copyright_>`_

------------

