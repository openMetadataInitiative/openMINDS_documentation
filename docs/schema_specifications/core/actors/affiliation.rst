###########
Affiliation
###########

:Semantic name: core:Affiliation

:Display as: Core:affiliation


------------

------------

Properties
##########

:Required: `memberOf <memberOf_heading_>`_
:Optional: `endDate <endDate_heading_>`_, `startDate <startDate_heading_>`_

------------

.. _endDate_heading:

*******
endDate
*******

Date in the Gregorian calendar at which something terminates in time.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the end date of this affiliation, formatted as 'YYYY-MM-DD'. Leave blank if this affiliation is still current.

`BACK TO TOP <Affiliation_>`_

------------

.. _memberOf_heading:

********
memberOf
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/memberOf
   :value type: | linked object of type
                | core:Consortium \[TYPE_ERROR\] or core:Organization \[TYPE_ERROR\]
   :instructions: Add the organization or consortium another party was or still is a member of.

`BACK TO TOP <Affiliation_>`_

------------

.. _startDate_heading:

*********
startDate
*********

Date in the Gregorian calendar at which something begins in time

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the start date of this affiliation, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <Affiliation_>`_

------------

