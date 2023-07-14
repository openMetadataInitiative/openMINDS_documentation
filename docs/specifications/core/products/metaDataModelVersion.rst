####################
MetaDataModelVersion
####################

:Semantic name: https://openminds.ebrains.eu/core/MetaDataModelVersion


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `description <description_heading_>`_, `developers <developers_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `license <license_heading_>`_, `releaseDate <releaseDate_heading_>`_, `repository <repository_heading_>`_, `shortName <shortName_heading_>`_, `type <type_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_
:Optional: `author <author_heading_>`_, `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `developer <developer_heading_>`_, `hasAlternativeVersion <hasAlternativeVersion_heading_>`_, `hasSupplementVersion <hasSupplementVersion_heading_>`_, `homepage <homepage_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `otherContribution <otherContribution_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `serializationFormat <serializationFormat_heading_>`_, `specificationFormat <specificationFormat_heading_>`_, `versionInnovation <versionInnovation_heading_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/accessibility
   :value type: | linked object of type
                | `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/productAccessibility.html>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/author
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/person.html>`_
   :instructions: Add one or several authors (person or organization) that contributed to the production and publication of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/copyright.html>`_
   :instructions: Add the copyright information of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/person.html>`_
   :instructions: Add one or several custodians (person or organization) that are responsible for this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

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
   :instructions: Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references).

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _developer_heading:

*********
developer
*********

Legal person that creates or improves products or services (e.g., software, applications, etc.).

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/developer
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/person.html>`_
   :instructions: Add one or several developers (person or organization) that contributed to the code implementation of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _fullDocumentation_heading:

*****************
fullDocumentation
*****************

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullDocumentation
   :value type: | linked object of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add the globally unique and persistent digital identifier of a full documentation of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

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
   :instructions: Enter a descriptive full name (title) for this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _hasAlternativeVersion_heading:

*********************
hasAlternativeVersion
*********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasAlternativeVersion
   :value type: | linked object array \(1-N\) of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/products/datasetVersion.html>`_
   :instructions: Add all (meta)data model versions that can be used alternatively to this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _hasSupplementVersion_heading:

********************
hasSupplementVersion
********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasSupplementVersion
   :value type: | linked object array \(1-N\) of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/products/datasetVersion.html>`_
   :instructions: Add all (meta)data model versions that supplement this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/products/metaDataModelVersion.html>`_
   :instructions: Add the dataset version preceding this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | string array \(1-5\)
                | formatting: text/plain; singleline
   :instructions: Enter custom keywords to this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object of type
                | `License <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/license.html>`_
   :instructions: Add the license of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _otherContribution_heading:

*****************
otherContribution
*****************

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherContribution
   :value type: | linked object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/actors/contribution.html>`_
   :instructions: Add the contributions for each involved person or organization going beyond being an author, custodian or developer of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add further publications besides the documentation (e.g. an original research article) providing the original context for the production of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) of the first broadcast/publication of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/fileRepository.html>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _serializationFormat_heading:

*******************
serializationFormat
*******************

Form in which a particular data structure or object state is translated to for storage.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/serializationFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/contentType.html>`_
   :instructions: Add all content types in which (meta)data compliant with this (meta)data model version can be stored in.

`BACK TO TOP <MetaDataModelVersion_>`_

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
   :instructions: Enter a short name (alias) for this research product version (max. 30 characters, no space).

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _specificationFormat_heading:

*******************
specificationFormat
*******************

Form in which a particular data structure or object state is specified in.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specificationFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/data/contentType.html>`_
   :instructions: Add all content types in which the schemas of this (meta)data model version are stored in.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/metaDataModelType.html>`_
   :instructions: Add the type of this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short summary of the novelties/peculiarities of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

