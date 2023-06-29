######
Person
######

****************************************
https://openminds.ebrains.eu/core/Person
****************************************

Structured information on a person.

Properties
==========

:Required: `givenName`_
:Optional: `affiliation`_, `alternateName`_, `associatedAccount`_, `contactInformation`_, `digitalIdentifier`_, `familyName`_

------------

affiliation
-----------

Declaration of a person being closely associated to an organization.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/affiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds.ebrains.eu/core/Affiliation>`_
   :instructions: Enter all current and, if desired, past affiliations of this person.

`BACK TO TOP <Person_>`_

------------

alternateName
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/alternateName
   :value type: string array \(1-N\)
   :instructions: Enter any other known full name of this person.

`BACK TO TOP <Person_>`_

------------

associatedAccount
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/associatedAccount
   :value type: | linked object array \(1-N\) of type
                | `AccountInformation <https://openminds.ebrains.eu/core/AccountInformation>`_
   :instructions: Add the information about web service accounts held by this person.

`BACK TO TOP <Person_>`_

------------

contactInformation
------------------

Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactInformation
   :value type: | linked object of type
                | `ContactInformation <https://openminds.ebrains.eu/core/ContactInformation>`_
   :instructions: Add the contact information of this person.

`BACK TO TOP <Person_>`_

------------

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `ORCID <https://openminds.ebrains.eu/core/ORCID>`_
   :instructions: Add all globally unique and persistent digital identifier of this person.

`BACK TO TOP <Person_>`_

------------

familyName
----------

Name borne in common by members of a family.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/familyName
   :value type: string
   :instructions: Enter the family name of this person.

`BACK TO TOP <Person_>`_

------------

givenName
---------

Name given to a person, including all potential middle names, but excluding the family name.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/givenName
   :value type: string
   :instructions: Enter the given name of this person.

`BACK TO TOP <Person_>`_

------------
