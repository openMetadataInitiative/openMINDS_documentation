######
Person
######

****************************************
https://openminds.ebrains.eu/core/Person
****************************************

Structured information on a person.

**********
Properties
**********

:Required: `givenName <givenName_heading_>`_
:Optional: `affiliation <affiliation_heading_>`_, `alternateName <alternateName_heading_>`_, `associatedAccount <associatedAccount_heading_>`_,
   `contactInformation <contactInformation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `familyName <familyName_heading_>`_

------------

.. _https://openminds.ebrains.eu/vocab/affiliation_heading:

https://openminds.ebrains.eu/vocab/affiliation
----------------------------------------------

Declaration of a person being closely associated to an organization.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/affiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds.ebrains.eu/core/Affiliation>`_
   :instructions: Enter all current and, if desired, past affiliations of this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/alternateName_heading:

https://openminds.ebrains.eu/vocab/alternateName
------------------------------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/alternateName
   :value type: string array \(1-N\)
   :instructions: Enter any other known full name of this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/associatedAccount_heading:

https://openminds.ebrains.eu/vocab/associatedAccount
----------------------------------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/associatedAccount
   :value type: | linked object array \(1-N\) of type
                | `AccountInformation <https://openminds.ebrains.eu/core/AccountInformation>`_
   :instructions: Add the information about web service accounts held by this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/contactInformation_heading:

https://openminds.ebrains.eu/vocab/contactInformation
-----------------------------------------------------

Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/contactInformation
   :value type: | linked object of type
                | `ContactInformation <https://openminds.ebrains.eu/core/ContactInformation>`_
   :instructions: Add the contact information of this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/digitalIdentifier_heading:

https://openminds.ebrains.eu/vocab/digitalIdentifier
----------------------------------------------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `ORCID <https://openminds.ebrains.eu/core/ORCID>`_
   :instructions: Add all globally unique and persistent digital identifier of this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/familyName_heading:

https://openminds.ebrains.eu/vocab/familyName
---------------------------------------------

Name borne in common by members of a family.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/familyName
   :value type: string
   :instructions: Enter the family name of this person.

`BACK TO TOP <Person_>`_

------------

.. _https://openminds.ebrains.eu/vocab/givenName_heading:

https://openminds.ebrains.eu/vocab/givenName
--------------------------------------------

Name given to a person, including all potential middle names, but excluding the family name.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/https://openminds.ebrains.eu/vocab/givenName
   :value type: string
   :instructions: Enter the given name of this person.

`BACK TO TOP <Person_>`_

------------
