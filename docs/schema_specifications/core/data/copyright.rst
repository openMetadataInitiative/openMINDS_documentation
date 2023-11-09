#########
Copyright
#########

:Semantic name: https://openminds.ebrains.eu/core/Copyright

Structured information on the copyright.


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
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add one or several persons or organisations that hold the copyright.

`BACK TO TOP <Copyright_>`_

------------

.. _year_heading:

****
year
****

Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/year
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the year during which the copyright was first asserted.

`BACK TO TOP <Copyright_>`_

------------

