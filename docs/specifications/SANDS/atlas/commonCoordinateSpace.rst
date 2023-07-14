#####################
CommonCoordinateSpace
#####################

:Semantic name:: https://openminds.ebrains.eu/sands/CommonCoordinateSpace


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasVersion <hasVersion_heading_>`_, `shortName <shortName_heading_>`_, `usedSpecies <usedSpecies_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `author <author_heading_>`_, `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this common coordinate space.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/author
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_
   :instructions: Add all parties that contributed to this common coordinate space as authors.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_
   :instructions: Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/DOI.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/ISBN.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _hasVersion_heading:

**********
hasVersion
**********

Reference to variants of an original.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasVersion
   :value type: | linked object array \(1-N\) of type
                | `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add all versions of this common coordinate space.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

.. _usedSpecies_heading:

***********
usedSpecies
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecies
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_
   :instructions: Add the species that was used for the creation of this common coordinate space.

`BACK TO TOP <CommonCoordinateSpace_>`_

------------

