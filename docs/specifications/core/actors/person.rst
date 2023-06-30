######
Person
######

https://openminds.ebrains.eu/core/Person
----------------------------------------

Structured information on a person.

------------

------------

**********
Properties
**********

:Required: `email <email_heading_>`_, `givenName <givenName_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `familyName <familyName_heading_>`_

------------

.. _digitalIdentifier_heading:

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add one or several globally unique and persistent digital identifier for this person.

`BACK TO TOP <Person_>`_

------------

.. _email_heading:

email
-----

Address to which or from which an electronic mail can be sent.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/email
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the email address of this person.

`BACK TO TOP <Person_>`_

------------

.. _familyName_heading:

familyName
----------

Name borne in common by members of a family.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/familyName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the family name of this person.

`BACK TO TOP <Person_>`_

------------

.. _givenName_heading:

givenName
---------

Name given to a person, including all potential middle names, but excluding the family name.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/givenName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the given name of this person.

`BACK TO TOP <Person_>`_

------------

