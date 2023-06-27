Person
######

https://openminds.ebrains.eu/core/Person
****************************************

Structured information on a person.

------------ 

**Properties**
==============

..
   .. note::
      Properties are displayed with their simple name ("simplePropertyName"). Within an openMINDS metadata instance (JSON-LD) the property name has to be extended to the full openMINDS namespace          ("https://openminds.ebrains.eu/vocab/simplePropertyName"). 

**affiliation** ``(array, item: embedded object)``
--------------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **description:** Declaration of a person being closely associated to an organization.
|   - **instruction:** Enter all current and, if desired, past affiliations of this person.
|   - **objectTypes:** `Affiliation <https://openminds.ebrains.eu/core/Affiliation>`_

| **alternateName** ``(array, item: string)``
---------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **instruction:** Enter any other known full name of this person.

| **associatedAccount** ``(array, item: linked object)``
--------------------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **instruction:** Add the information about web service accounts held by this person.
|   - **objectTypes:** `AccountInformation <https://openminds.ebrains.eu/core/AccountInformation>`_

| **contactInformation** ``(array, item: linked object)``
---------------------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **description:** Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).
|   - **instruction:** Add the contact information of this person.
|   - **objectTypes:** `ContactInformation <https://openminds.ebrains.eu/core/ContactInformation>`_

| **digitalIdentifier** ``(array, item: linked object)``
--------------------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **description:** Digital handle to identify objects or legal persons.
|   - **instruction:** Add all globally unique and persistent digital identifier of this person.
|   - **objectTypes:** `ORCID <https://openminds.ebrains.eu/core/ORCID>`_

| **familyName** ``(array, item: string)``
------------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **description:** Name borne in common by members of a family.
|   - **instruction:** Enter the family name of this person.

| **givenName** ``(array, item: string)``
-----------------------------------------
| https://openminds.ebrains.eu/vocab/affiliation
|   - **description:** Name given to a person, including all potential middle names, but excluding the family name.
|   - **instruction:** Enter the given name of this person.
