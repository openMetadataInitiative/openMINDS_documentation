Person
======

https://openminds.ebrains.eu/core/Person
----------------------------------------

Structured information on a person.

------------ 

**Properties**

Note: properties are displayed with their simple name ("simplePropertyName"). Within an openMINDS metadata instance (JSON-LD) the property name has to be extended to the full openMINDS namespace ("https://openminds.ebrains.eu/vocab/simplePropertyName"). 

  | **affiliation** (array, item: embedded object)
  |   - **description:** Declaration of a person being closely associated to an organization.
  |   - **instruction:** Enter all current and, if desired, past affiliations of this person.
  |   - **objectTypes:** `Affiliation <https://openminds.ebrains.eu/core/Affiliation>`_
  
  | **alternateName** (array, item: string)
  |   - **instruction:** Enter any other known full name of this person.

  | **associatedAccount** (array, item: linked object)
  |   - **instruction:** Add the information about web service accounts held by this person.
  |   - **objectTypes:** `AccountInformation <https://openminds.ebrains.eu/core/AccountInformation>`_
  
  | **contactInformation** (array, item: linked object)
  |   - **description:** Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).
  |   - **instruction:** Add the contact information of this person.
  |   - **objectTypes:** `ContactInformation <https://openminds.ebrains.eu/core/ContactInformation>`_
