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
:Optional: `affiliation`_, `alternateName`_, `associatedAccount`_,
   `contactInformation`_, `digitalIdentifier`_, `familyName`_

------------

affiliation
-----------

Declaration of a person being closely associated to an organization.

:Semantic name: https://openminds.ebrains.eu/vocab/affiliation

:Value type: | embedded object array of type
             | `Affiliation
<https://openminds.ebrains.eu/core/Affiliation>`_

.. Instructions::
   Enter all current and, if desired, past affiliations of this person.


------------

alternateName
-------------

:Semantic name: https://openminds.ebrains.eu/vocab/alternateName

:Value type: string array

.. Instructions::
   Enter any other known full name of this person.


------------

associatedAccount
-----------------

:Semantic name: https://openminds.ebrains.eu/vocab/associatedAccount

:Value type: | linked object array of type
             | `AccountInformation
<https://openminds.ebrains.eu/core/AccountInformation>`_

.. Instructions::
   Add the information about web service accounts held by this person.


------------

contactInformation
------------------

Any available way used to contact a person or business (e.g., address,
phone number, email address, etc.).

:Semantic name: https://openminds.ebrains.eu/vocab/contactInformation

:Value type: | linked object of type
             | `ContactInformation
<https://openminds.ebrains.eu/core/ContactInformation>`_

.. Instructions::
   Add the contact information of this person.


------------

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

:Semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier

:Value type: | linked object array of type
             | `ORCID <https://openminds.ebrains.eu/core/ORCID>`_

.. Instructions::
   Add all globally unique and persistent digital identifier of this
   person.


------------

familyName
----------

Name borne in common by members of a family.

:Semantic name: https://openminds.ebrains.eu/vocab/familyName

:Value type: string

.. Instructions::
   Enter the family name of this person.


------------

givenName
---------

Name given to a person, including all potential middle names, but
excluding the family name.

:Semantic name: https://openminds.ebrains.eu/vocab/givenName

:Value type: string

.. Instructions::

   Enter the given name of this person.


------------
