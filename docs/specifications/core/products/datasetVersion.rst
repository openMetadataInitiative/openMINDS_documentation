##############
DatasetVersion
##############

:Semantic name: https://openminds.ebrains.eu/core/DatasetVersion

Structured information on data originating from human/animal studies or simulations (version level).


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `dataType <dataType_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `ethicsAssessment <ethicsAssessment_heading_>`_, `experimentalApproach <experimentalApproach_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `license <license_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `technique <technique_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `author <author_heading_>`_, `behavioralProtocol <behavioralProtocol_heading_>`_, `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `description <description_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `inputData <inputData_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `otherContribution <otherContribution_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `protocol <protocol_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `studiedSpecimen <studiedSpecimen_heading_>`_, `studyTarget <studyTarget_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/accessibility
   :value type: | linked object of type
                | `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/productAccessibility.html>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Add all parties that contributed to this dataset version as authors. Note that these authors will overwrite the author list provided for the overarching dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _behavioralProtocol_heading:

******************
behavioralProtocol
******************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/behavioralProtocol
   :value type: | linked object array \(1-N\) of type
                | `BehavioralProtocol <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/behavioralProtocol.html>`_
   :instructions: Add all behavioral protocols that were performed in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/copyright.html>`_
   :instructions: Enter the copyright information of this research product version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataType
   :value type: | linked object array \(1-N\) of type
                | `SemanticDataType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/semanticDataType.html>`_
   :instructions: Add all semantic data types (raw, derived and/or simulated) provided in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/DOI.html>`_ or `IdentifiersDotOrgID <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/IdentifiersDotOrgID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _ethicsAssessment_heading:

****************
ethicsAssessment
****************

Judgment about the applied principles of conduct governing an individual or a group.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ethicsAssessment
   :value type: | linked object of type
                | `EthicsAssessment <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/ethicsAssessment.html>`_
   :instructions: Add the result of the ethics assessment of this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _experimentalApproach_heading:

********************
experimentalApproach
********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/experimentalApproach
   :value type: | linked object array \(1-N\) of type
                | `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/experimentalApproach.html>`_
   :instructions: Add all experimental approaches which this dataset version has deployed.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _fullDocumentation_heading:

*****************
fullDocumentation
*****************

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullDocumentation
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the publication or file that acts as the full documentation of this research product version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <DatasetVersion_>`_

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

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _inputData_heading:

*********
inputData
*********

Data that is put into a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inputData
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileBundle.html>`_, `WebResource <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/webResource.html>`_, `BrainAtlas <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/brainAtlas.html>`_, `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/brainAtlasVersion.html>`_, `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add the data that was used as input for this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/products/datasetVersion.html>`_
   :instructions: Add all dataset versions that can be used alternatively to this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version preceding this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | linked object array \(1-N\) of type
                | `ActionStatusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/actionStatusType.html>`_, `AgeCategory <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/ageCategory.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/analysisTechnique.html>`_, `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/anatomicalAxesOrientation.html>`_, `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/anatomicalIdentificationType.html>`_, `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/anatomicalPlane.html>`_, `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/annotationCriteriaType.html>`_, `AnnotationType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/annotationType.html>`_, `AtlasType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/atlasType.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/chemicalMixtureType.html>`_, `Colormap <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/colormap.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/contributionType.html>`_, `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cranialWindowConstructionType.html>`_, `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cranialWindowReinforcementType.html>`_, `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/criteriaQualityType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/dataType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/deviceType.html>`_, `DifferenceMeasure <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/differenceMeasure.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/diseaseModel.html>`_, `EducationalLevel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/educationalLevel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/electricalStimulusType.html>`_, `EthicsAssessment <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/ethicsAssessment.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/experimentalApproach.html>`_, `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/fileBundleGrouping.html>`_, `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/fileRepositoryType.html>`_, `FileUsageRole <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/fileUsageRole.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/handedness.html>`_, `Language <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/language.html>`_, `Laterality <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/laterality.html>`_, `LearningResourceType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/learningResourceType.html>`_, `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/measuredQuantity.html>`_, `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/metaDataModelType.html>`_, `ModelAbstractionLevel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/modelAbstractionLevel.html>`_, `ModelScope <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/modelScope.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/olfactoryStimulusType.html>`_, `OperatingDevice <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/operatingDevice.html>`_, `OperatingSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/operatingSystem.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSystem.html>`_, `PatchClampVariation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/patchClampVariation.html>`_, `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/preparationType.html>`_, `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/productAccessibility.html>`_, `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/programmingLanguage.html>`_, `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/qualitativeOverlap.html>`_, `SemanticDataType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/semanticDataType.html>`_, `Service <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/service.html>`_, `SetupType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/setupType.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/softwareFeature.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subjectAttribute.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/termSuggestion.html>`_, `Terminology <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/terminology.html>`_, `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tissueSampleAttribute.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tissueSampleType.html>`_, `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/typeOfUncertainty.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/unitOfMeasurement.html>`_ or `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/visualStimulusType.html>`_
   :instructions: Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object of type
                | `License <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/license.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the license or an online available data usage agreement for this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _otherContribution_heading:

*****************
otherContribution
*****************

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherContribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/contribution.html>`_
   :instructions: Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _preparationDesign_heading:

*****************
preparationDesign
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationDesign
   :value type: | linked object array \(1-N\) of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/preparationType.html>`_
   :instructions: Add all preparation types used in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/protocol.html>`_
   :instructions: Add all protocols that were performed in this dataset version (e.g., for data acquisition or processing).

`BACK TO TOP <DatasetVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/DOI.html>`_, `HANDLE <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/HANDLE.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/ISBN.html>`_, `ISSN <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/digitalIdentifier/ISSN.html>`_, `Book <https://openminds-documentation.readthedocs.io/en/latest/specifications/publications/book.html>`_, `Chapter <https://openminds-documentation.readthedocs.io/en/latest/specifications/publications/chapter.html>`_ or `ScholarlyArticle <https://openminds-documentation.readthedocs.io/en/latest/specifications/publications/scholarlyArticle.html>`_
   :instructions: Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileRepository.html>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <DatasetVersion_>`_

------------

.. _studiedSpecimen_heading:

***************
studiedSpecimen
***************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedSpecimen
   :value type: | linked object array \(1-N\) of type
                | `Subject <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subject.html>`_, `SubjectGroup <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectGroup.html>`_, `TissueSample <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSample.html>`_ or `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleCollection.html>`_
   :instructions: Add all specimens or sets of specimen that were studied in this dataset.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/electricalStimulusType.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSystem.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tactileStimulusType.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/termSuggestion.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/visualStimulusType.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all study targets of this dataset version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product version.

`BACK TO TOP <DatasetVersion_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/analysisTechnique.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationTechnique.html>`_ or `Technique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/technique.html>`_
   :instructions: Add all techniques that were used in this dataset version.

`BACK TO TOP <DatasetVersion_>`_

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

`BACK TO TOP <DatasetVersion_>`_

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
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.

`BACK TO TOP <DatasetVersion_>`_

------------

