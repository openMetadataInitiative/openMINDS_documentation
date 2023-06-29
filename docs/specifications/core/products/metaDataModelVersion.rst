####################
MetaDataModelVersion
####################

https://openminds.ebrains.eu/core/MetaDataModelVersion
------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `accessibility <accessibility_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `license <license_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `type <type_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `description <description_heading_>`_, `developer <developer_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `otherContribution <otherContribution_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `serializationFormat <serializationFormat_heading_>`_, `specificationFormat <specificationFormat_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _accessibility_heading:

accessibility
-------------

Level to which something is accessible to someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/accessibility
   :value type: | linked object of type
                | `ProductAccessibility <https://openminds.ebrains.eu/controlledTerms/ProductAccessibility>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _copyright_heading:

copyright
---------

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds.ebrains.eu/core/Copyright>`_
   :instructions: Enter the copyright information of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _custodian_heading:

custodian
---------

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _developer_heading:

developer
---------

Legal person that creates or improves products or services (e.g., software, applications, etc.).

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/developer
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that developed this (meta)data model version. Note that these developers will overwrite the developer list provided for the overarching (meta)data model.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _digitalIdentifier_heading:

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_ or `SWHID <https://openminds.ebrains.eu/core/SWHID>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _fullDocumentation_heading:

fullDocumentation
-----------------

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullDocumentation
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_, `File <https://openminds.ebrains.eu/core/File>`_ or `WebResource <https://openminds.ebrains.eu/core/WebResource>`_
   :instructions: Add the publication or file that acts as the full documentation of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _fullName_heading:

fullName
--------

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _funding_heading:

funding
-------

Money provided by a legal person for a particular purpose.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds.ebrains.eu/core/Funding>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _homepage_heading:

homepage
--------

Main website of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _howToCite_heading:

howToCite
---------

Preferred format for citing a particular object or legal person.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

isAlternativeVersionOf
----------------------

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_
   :instructions: Add all (meta)data model versions that can be used alternatively to this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _isNewVersionOf_heading:

isNewVersionOf
--------------

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_
   :instructions: Add the (meta)data version preceding this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _keyword_heading:

keyword
-------

Significant word or concept that are representative of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | linked object array \(1-N\) of type
                | `ActionStatusType <https://openminds.ebrains.eu/controlledTerms/ActionStatusType>`_, `AgeCategory <https://openminds.ebrains.eu/controlledTerms/AgeCategory>`_, `AnalysisTechnique <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_, `AnatomicalAxesOrientation <https://openminds.ebrains.eu/controlledTerms/AnatomicalAxesOrientation>`_, `AnatomicalIdentificationType <https://openminds.ebrains.eu/controlledTerms/AnatomicalIdentificationType>`_, `AnatomicalPlane <https://openminds.ebrains.eu/controlledTerms/AnatomicalPlane>`_, `AnnotationCriteriaType <https://openminds.ebrains.eu/controlledTerms/AnnotationCriteriaType>`_, `AnnotationType <https://openminds.ebrains.eu/controlledTerms/AnnotationType>`_, `AtlasType <https://openminds.ebrains.eu/controlledTerms/AtlasType>`_, `AuditoryStimulusType <https://openminds.ebrains.eu/controlledTerms/AuditoryStimulusType>`_, `BiologicalOrder <https://openminds.ebrains.eu/controlledTerms/BiologicalOrder>`_, `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_, `BreedingType <https://openminds.ebrains.eu/controlledTerms/BreedingType>`_, `CellCultureType <https://openminds.ebrains.eu/controlledTerms/CellCultureType>`_, `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `ChemicalMixtureType <https://openminds.ebrains.eu/controlledTerms/ChemicalMixtureType>`_, `Colormap <https://openminds.ebrains.eu/controlledTerms/Colormap>`_, `ContributionType <https://openminds.ebrains.eu/controlledTerms/ContributionType>`_, `CranialWindowConstructionType <https://openminds.ebrains.eu/controlledTerms/CranialWindowConstructionType>`_, `CranialWindowReinforcementType <https://openminds.ebrains.eu/controlledTerms/CranialWindowReinforcementType>`_, `CriteriaQualityType <https://openminds.ebrains.eu/controlledTerms/CriteriaQualityType>`_, `DataType <https://openminds.ebrains.eu/controlledTerms/DataType>`_, `DeviceType <https://openminds.ebrains.eu/controlledTerms/DeviceType>`_, `DifferenceMeasure <https://openminds.ebrains.eu/controlledTerms/DifferenceMeasure>`_, `Disease <https://openminds.ebrains.eu/controlledTerms/Disease>`_, `DiseaseModel <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_, `EducationalLevel <https://openminds.ebrains.eu/controlledTerms/EducationalLevel>`_, `ElectricalStimulusType <https://openminds.ebrains.eu/controlledTerms/ElectricalStimulusType>`_, `EthicsAssessment <https://openminds.ebrains.eu/controlledTerms/EthicsAssessment>`_, `ExperimentalApproach <https://openminds.ebrains.eu/controlledTerms/ExperimentalApproach>`_, `FileBundleGrouping <https://openminds.ebrains.eu/controlledTerms/FileBundleGrouping>`_, `FileRepositoryType <https://openminds.ebrains.eu/controlledTerms/FileRepositoryType>`_, `FileUsageRole <https://openminds.ebrains.eu/controlledTerms/FileUsageRole>`_, `GeneticStrainType <https://openminds.ebrains.eu/controlledTerms/GeneticStrainType>`_, `GustatoryStimulusType <https://openminds.ebrains.eu/controlledTerms/GustatoryStimulusType>`_, `Handedness <https://openminds.ebrains.eu/controlledTerms/Handedness>`_, `Language <https://openminds.ebrains.eu/controlledTerms/Language>`_, `Laterality <https://openminds.ebrains.eu/controlledTerms/Laterality>`_, `LearningResourceType <https://openminds.ebrains.eu/controlledTerms/LearningResourceType>`_, `MeasuredQuantity <https://openminds.ebrains.eu/controlledTerms/MeasuredQuantity>`_, `MetaDataModelType <https://openminds.ebrains.eu/controlledTerms/MetaDataModelType>`_, `ModelAbstractionLevel <https://openminds.ebrains.eu/controlledTerms/ModelAbstractionLevel>`_, `ModelScope <https://openminds.ebrains.eu/controlledTerms/ModelScope>`_, `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_, `OlfactoryStimulusType <https://openminds.ebrains.eu/controlledTerms/OlfactoryStimulusType>`_, `OperatingDevice <https://openminds.ebrains.eu/controlledTerms/OperatingDevice>`_, `OperatingSystem <https://openminds.ebrains.eu/controlledTerms/OperatingSystem>`_, `OpticalStimulusType <https://openminds.ebrains.eu/controlledTerms/OpticalStimulusType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_, `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `OrganismSystem <https://openminds.ebrains.eu/controlledTerms/OrganismSystem>`_, `PatchClampVariation <https://openminds.ebrains.eu/controlledTerms/PatchClampVariation>`_, `PreparationType <https://openminds.ebrains.eu/controlledTerms/PreparationType>`_, `ProductAccessibility <https://openminds.ebrains.eu/controlledTerms/ProductAccessibility>`_, `ProgrammingLanguage <https://openminds.ebrains.eu/controlledTerms/ProgrammingLanguage>`_, `QualitativeOverlap <https://openminds.ebrains.eu/controlledTerms/QualitativeOverlap>`_, `SemanticDataType <https://openminds.ebrains.eu/controlledTerms/SemanticDataType>`_, `Service <https://openminds.ebrains.eu/controlledTerms/Service>`_, `SetupType <https://openminds.ebrains.eu/controlledTerms/SetupType>`_, `SoftwareApplicationCategory <https://openminds.ebrains.eu/controlledTerms/SoftwareApplicationCategory>`_, `SoftwareFeature <https://openminds.ebrains.eu/controlledTerms/SoftwareFeature>`_, `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_, `StimulationApproach <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_, `StimulationTechnique <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_, `SubcellularEntity <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `SubjectAttribute <https://openminds.ebrains.eu/controlledTerms/SubjectAttribute>`_, `TactileStimulusType <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_, `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_, `TermSuggestion <https://openminds.ebrains.eu/controlledTerms/TermSuggestion>`_, `Terminology <https://openminds.ebrains.eu/controlledTerms/Terminology>`_, `TissueSampleAttribute <https://openminds.ebrains.eu/controlledTerms/TissueSampleAttribute>`_, `TissueSampleType <https://openminds.ebrains.eu/controlledTerms/TissueSampleType>`_, `TypeOfUncertainty <https://openminds.ebrains.eu/controlledTerms/TypeOfUncertainty>`_, `UBERONParcellation <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `UnitOfMeasurement <https://openminds.ebrains.eu/controlledTerms/UnitOfMeasurement>`_ or `VisualStimulusType <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_
   :instructions: Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _license_heading:

license
-------

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object of type
                | `License <https://openminds.ebrains.eu/core/License>`_
   :instructions: Add the license of this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _otherContribution_heading:

otherContribution
-----------------

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherContribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds.ebrains.eu/core/Contribution>`_
   :instructions: Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _relatedPublication_heading:

relatedPublication
------------------

Reference to something that was made available for the general public to see or buy.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_, `HANDLE <https://openminds.ebrains.eu/core/HANDLE>`_, `ISBN <https://openminds.ebrains.eu/core/ISBN>`_, `ISSN <https://openminds.ebrains.eu/core/ISSN>`_, `Book <https://openminds.ebrains.eu/publications/Book>`_, `Chapter <https://openminds.ebrains.eu/publications/Chapter>`_ or `ScholarlyArticle <https://openminds.ebrains.eu/publications/ScholarlyArticle>`_
   :instructions: Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _releaseDate_heading:

releaseDate
-----------

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _repository_heading:

repository
----------

Place, room, or container where something is deposited or stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds.ebrains.eu/core/FileRepository>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _serializationFormat_heading:

serializationFormat
-------------------

Form in which a particular data structure or object state is translated to for storage.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/serializationFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: Add all content types in which (meta)data compliant with this (meta)data model version can be stored in.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _shortName_heading:

shortName
---------

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _specificationFormat_heading:

specificationFormat
-------------------

Form in which a particular data structure or object state is specified in.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specificationFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: Add all content types in which the schemas of this (meta)data model version are stored in.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _supportChannel_heading:

supportChannel
--------------

Way of communication used to interact with users or customers.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _type_heading:

type
----

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | `MetaDataModelType <https://openminds.ebrains.eu/controlledTerms/MetaDataModelType>`_
   :instructions: Add the type of this (meta)data model version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _versionIdentifier_heading:

versionIdentifier
-----------------

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

.. _versionInnovation_heading:

versionInnovation
-----------------

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.

`BACK TO TOP <MetaDataModelVersion_>`_

------------

