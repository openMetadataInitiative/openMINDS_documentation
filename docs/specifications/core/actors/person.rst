######
Person
######

****************************************
https://openminds.ebrains.eu/core/Person
****************************************

Structured information on a person.

==========
Properties
==========
:Required: `givenName`_
:Optional: `affiliation`_, `alternateName`_, `associatedAccount`_, `contactInformation`_, `digitalIdentifier`_, `familyName`_
==========

------------ 

.. topic:: affiliation

  :Description: Declaration of a person being closely associated to an organization.
  :Format: array; item: embedded object
  :Instruction: Enter all current and, if desired, past affiliations of this person.
  :Object types: `Affiliation <https://openminds.ebrains.eu/core/Affiliation>`_
  :Vocab: ``"https://openminds.ebrains.eu/vocab/affiliation"``

alternateName
-------------
:vocab: ``"https://openminds.ebrains.eu/vocab/alternateName"``
:format: array; item: string
:instruction: Enter any other known full name of this person.

associatedAccount
-----------------
:vocab: ``"https://openminds.ebrains.eu/vocab/associatedAccount"``
:format: array; item: linked object
:instruction: Add the information about web service accounts held by this person.
:objectTypes: `AccountInformation <https://openminds.ebrains.eu/core/AccountInformation>`_

contactInformation
------------------
:vocab: ``"https://openminds.ebrains.eu/vocab/contactInformation"``
:description: Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).
:instruction: Add the contact information of this person.
:objectTypes: `ContactInformation <https://openminds.ebrains.eu/core/ContactInformation>`_

digitalIdentifier
-----------------
:vocab: ``"https://openminds.ebrains.eu/vocab/digitalIdentifier"``
:format: array: 1-N items; item: linked object
:description: Digital handle to identify objects or legal persons.
:instruction: Add all globally unique and persistent digital identifier of this person.
:objectTypes: `ORCID <https://openminds.ebrains.eu/core/ORCID>`_

familyName
----------
:vocab: ``"https://openminds.ebrains.eu/vocab/familyName"``
:format: string
:description: Name borne in common by members of a family.
:instruction: Enter the family name of this person.

givenName
---------
:vocab: ``"https://openminds.ebrains.eu/vocab/givenName"``
:format: string
:description: Name given to a person, including all potential middle names, but excluding the family name.
:instruction: Enter the given name of this person.
