###########
Affiliation
###########

*********************************************
https://openminds.ebrains.eu/core/Affiliation
*********************************************

Structured information about a relationship between two entities, such as a person and their employer.

------------

------------

**********
Properties
**********

:Required: `memberOf <memberOf_heading_>`_
:Optional: `endDate <endDate_heading_>`_, `startDate <startDate_heading_>`_

------------

.. _endDate_heading:

endDate
-------

Date in the Gregorian calendar at which something terminates in time.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the end date of this affiliation, formatted as 'YYYY-MM-DD'. Leave blank if this affiliation is still current.

`BACK TO TOP <Affiliation_>`_

------------

.. _memberOf_heading:

memberOf
--------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/memberOf
   :value type: | linked object of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_or `Organization <https://openminds.ebrains.eu/core/Organization>`_
   :instructions: Add the organization or consortium another party was or still is a member of.

`BACK TO TOP <Affiliation_>`_

------------

.. _startDate_heading:

startDate
---------

Date in the Gregorian calendar at which something begins in time

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the start date of this affiliation, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <Affiliation_>`_

------------

