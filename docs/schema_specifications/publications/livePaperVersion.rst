################
LivePaperVersion
################

:Semantic name: publications:LivePaperVersion

:Display as: Publications:live paper version


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `license <license_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `about <about_heading_>`_, `author <author_heading_>`_, `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `description <description_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `modificationDate <modificationDate_heading_>`_, `otherContribution <otherContribution_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _about_heading:

*****
about
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/about
   :value type: | linked object array \(1-N\) of type
                | core:DatasetVersion \[TYPE_ERROR\], core:ModelVersion \[TYPE_ERROR\] or core:SoftwareVersion \[TYPE_ERROR\]
   :instructions: Add all datasets, models and/or software that are part of or are described by this live paper version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/accessibility
   :value type: | linked object of type
                | controlledTerms:ProductAccessibility \[TYPE_ERROR\]
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/author
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that contributed to this live paper version as authors. Note that these authors will overwrite the author list provided for the overarching live paper.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | core:Copyright \[TYPE_ERROR\]
   :instructions: Enter the copyright information of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | core:DOI \[TYPE_ERROR\]
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _fullDocumentation_heading:

*****************
fullDocumentation
*****************

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullDocumentation
   :value type: | linked object of type
                | core:DOI \[TYPE_ERROR\], core:File \[TYPE_ERROR\], core:ISBN \[TYPE_ERROR\] or core:WebResource \[TYPE_ERROR\]
   :instructions: Add the publication or file that acts as the full documentation of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | core:Funding \[TYPE_ERROR\]
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | publications:LivePaperVersion \[TYPE_ERROR\]
   :instructions: Add all live paper versions that can be used alternatively to this live paper version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | publications:LivePaperVersion \[TYPE_ERROR\]
   :instructions: Add the live paper version preceding this live paper version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:ActionStatusType \[TYPE_ERROR\], controlledTerms:AgeCategory \[TYPE_ERROR\], controlledTerms:AnalysisTechnique \[TYPE_ERROR\], controlledTerms:AnatomicalAxesOrientation \[TYPE_ERROR\], controlledTerms:AnatomicalIdentificationType \[TYPE_ERROR\], controlledTerms:AnatomicalPlane \[TYPE_ERROR\], controlledTerms:AnnotationCriteriaType \[TYPE_ERROR\], controlledTerms:AnnotationType \[TYPE_ERROR\], controlledTerms:AtlasType \[TYPE_ERROR\], controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:BiologicalOrder \[TYPE_ERROR\], controlledTerms:BiologicalProcess \[TYPE_ERROR\], controlledTerms:BiologicalSex \[TYPE_ERROR\], controlledTerms:BreedingType \[TYPE_ERROR\], controlledTerms:CellCultureType \[TYPE_ERROR\], controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:ChemicalMixtureType \[TYPE_ERROR\], controlledTerms:Colormap \[TYPE_ERROR\], controlledTerms:ContributionType \[TYPE_ERROR\], controlledTerms:CranialWindowConstructionType \[TYPE_ERROR\], controlledTerms:CranialWindowReinforcementType \[TYPE_ERROR\], controlledTerms:CriteriaQualityType \[TYPE_ERROR\], controlledTerms:DataType \[TYPE_ERROR\], controlledTerms:DeviceType \[TYPE_ERROR\], controlledTerms:DifferenceMeasure \[TYPE_ERROR\], controlledTerms:Disease \[TYPE_ERROR\], controlledTerms:DiseaseModel \[TYPE_ERROR\], controlledTerms:EducationalLevel \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:EthicsAssessment \[TYPE_ERROR\], controlledTerms:ExperimentalApproach \[TYPE_ERROR\], controlledTerms:FileBundleGrouping \[TYPE_ERROR\], controlledTerms:FileRepositoryType \[TYPE_ERROR\], controlledTerms:FileUsageRole \[TYPE_ERROR\], controlledTerms:GeneticStrainType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:Handedness \[TYPE_ERROR\], controlledTerms:Language \[TYPE_ERROR\], controlledTerms:Laterality \[TYPE_ERROR\], controlledTerms:LearningResourceType \[TYPE_ERROR\], controlledTerms:MRIPulseSequence \[TYPE_ERROR\], controlledTerms:MRIWeighting \[TYPE_ERROR\], controlledTerms:MeasuredQuantity \[TYPE_ERROR\], controlledTerms:MeasuredSignalType \[TYPE_ERROR\], controlledTerms:MetaDataModelType \[TYPE_ERROR\], controlledTerms:ModelAbstractionLevel \[TYPE_ERROR\], controlledTerms:ModelScope \[TYPE_ERROR\], controlledTerms:MolecularEntity \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OperatingDevice \[TYPE_ERROR\], controlledTerms:OperatingSystem \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:OrganismSystem \[TYPE_ERROR\], controlledTerms:PatchClampVariation \[TYPE_ERROR\], controlledTerms:PreparationType \[TYPE_ERROR\], controlledTerms:ProductAccessibility \[TYPE_ERROR\], controlledTerms:ProgrammingLanguage \[TYPE_ERROR\], controlledTerms:QualitativeOverlap \[TYPE_ERROR\], controlledTerms:SemanticDataType \[TYPE_ERROR\], controlledTerms:Service \[TYPE_ERROR\], controlledTerms:SetupType \[TYPE_ERROR\], controlledTerms:SoftwareApplicationCategory \[TYPE_ERROR\], controlledTerms:SoftwareFeature \[TYPE_ERROR\], controlledTerms:Species \[TYPE_ERROR\], controlledTerms:StimulationApproach \[TYPE_ERROR\], controlledTerms:StimulationTechnique \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:SubjectAttribute \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\], controlledTerms:Technique \[TYPE_ERROR\], controlledTerms:TermSuggestion \[TYPE_ERROR\], controlledTerms:Terminology \[TYPE_ERROR\], controlledTerms:TissueSampleAttribute \[TYPE_ERROR\], controlledTerms:TissueSampleType \[TYPE_ERROR\], controlledTerms:TypeOfUncertainty \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], controlledTerms:UnitOfMeasurement \[TYPE_ERROR\] or controlledTerms:VisualStimulusType \[TYPE_ERROR\]
   :instructions: Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object of type
                | core:License \[TYPE_ERROR\]
   :instructions: Add the license of this live paper version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _modificationDate_heading:

****************
modificationDate
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/modificationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this live paper version was last modified, formatted as 'YYYY-MM-DDThh:mm:ssTZD' (e.g., '2023-02-07T16:00:00+00:00').

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _otherContribution_heading:

*****************
otherContribution
*****************

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherContribution
   :value type: | embedded object array \(1-N\) of type
                | core:Contribution \[TYPE_ERROR\]
   :instructions: Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | core:DOI \[TYPE_ERROR\], core:HANDLE \[TYPE_ERROR\], core:ISBN \[TYPE_ERROR\], core:ISSN \[TYPE_ERROR\], publications:Book \[TYPE_ERROR\], publications:Chapter \[TYPE_ERROR\] or publications:ScholarlyArticle \[TYPE_ERROR\]
   :instructions: Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repository
   :value type: | linked object of type
                | core:FileRepository \[TYPE_ERROR\]
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

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
   :instructions: Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <LivePaperVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.

`BACK TO TOP <LivePaperVersion_>`_

------------

