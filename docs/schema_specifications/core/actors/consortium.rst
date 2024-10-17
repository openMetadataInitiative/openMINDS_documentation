##########
Consortium
##########

:Semantic name: core:Consortium

:Display as: Core:consortium


------------

------------

Properties
##########

:Required: `fullName <fullName_heading_>`_
:Optional: `contactInformation <contactInformation_heading_>`_, `homepage <homepage_heading_>`_, `shortName <shortName_heading_>`_

------------

.. _contactInformation_heading:

******************
contactInformation
******************

Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactInformation
   :value type: | linked object of type
                | core:ContactInformation \[TYPE_ERROR\]
   :instructions: Add the contact information of this consortium.

`BACK TO TOP <Consortium_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the full name of this consortium.

`BACK TO TOP <Consortium_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this consortium.

`BACK TO TOP <Consortium_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this consortium that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <Consortium_>`_

------------

