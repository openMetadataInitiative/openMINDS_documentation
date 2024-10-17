###############
SoftwareVersion
###############

:Semantic name: core:SoftwareVersion

:Display as: Core:software version


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `applicationCategory <applicationCategory_heading_>`_, `device <device_heading_>`_, `feature <feature_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `language <language_heading_>`_, `license <license_heading_>`_, `operatingSystem <operatingSystem_heading_>`_, `programmingLanguage <programmingLanguage_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `description <description_heading_>`_, `developer <developer_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `hasPart <hasPart_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `inputFormat <inputFormat_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `otherContribution <otherContribution_heading_>`_, `outputFormat <outputFormat_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `requirement <requirement_heading_>`_, `supportChannel <supportChannel_heading_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _applicationCategory_heading:

*******************
applicationCategory
*******************

Distinct class that groups software programs which perform a similar task or set of tasks.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/applicationCategory
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:SoftwareApplicationCategory \[TYPE_ERROR\]
   :instructions: Add all categories to which this software version belongs.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _developer_heading:

*********
developer
*********

Legal person that creates or improves products or services (e.g., software, applications, etc.).

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/developer
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that developed this software version. Note that these developers will overwrite the developer list provided for the overarching software.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:OperatingDevice \[TYPE_ERROR\]
   :instructions: Add all operating devices compatible with this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | core:DOI \[TYPE_ERROR\], core:SWHID \[TYPE_ERROR\] or core:RRID \[TYPE_ERROR\]
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _feature_heading:

*******
feature
*******

Structure, form, or appearance that characterizes something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/feature
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:SoftwareFeature \[TYPE_ERROR\]
   :instructions: Add all distinguishing characteristics of this software version (e.g., performance, portability or functionality).

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | linked object array \(1-N\) of type
                | core:ModelVersion \[TYPE_ERROR\], core:SoftwareVersion \[TYPE_ERROR\], sands:BrainAtlasVersion \[TYPE_ERROR\] or sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\]
   :instructions: Add all software versions that supplement this software version.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _inputFormat_heading:

***********
inputFormat
***********

Format of data that is put into a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inputFormat
   :value type: | linked object array \(1-N\) of type
                | core:ContentType \[TYPE_ERROR\]
   :instructions: Add all content types that can be used as input by this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | core:SoftwareVersion \[TYPE_ERROR\]
   :instructions: Add all software versions that can be used alternatively to this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | core:SoftwareVersion \[TYPE_ERROR\]
   :instructions: Add the software version preceding this software version.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _language_heading:

********
language
********

System of communication (words, their pronunciation, and the methods of combining them) used and understood by a particular community.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/language
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:Language \[TYPE_ERROR\]
   :instructions: Add all languages supported by this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object array \(1-N\) of type
                | core:License \[TYPE_ERROR\]
   :instructions: Add all licenses of this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _operatingSystem_heading:

***************
operatingSystem
***************

Software that controls the operation of a computer and directs the processing of programs.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/operatingSystem
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:OperatingSystem \[TYPE_ERROR\]
   :instructions: Add all operating systems supported by this software version.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _outputFormat_heading:

************
outputFormat
************

Format of data that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/outputFormat
   :value type: | linked object array \(1-N\) of type
                | core:ContentType \[TYPE_ERROR\]
   :instructions: Add all content types that can be generated as output by this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _programmingLanguage_heading:

*******************
programmingLanguage
*******************

Distinct set of instructions for computer programs in order to produce various kinds of output.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/programmingLanguage
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:ProgrammingLanguage \[TYPE_ERROR\]
   :instructions: Add all programming languages used to develop this software version.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _requirement_heading:

***********
requirement
***********

Something essential to the existence, occurrence or function of something else.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/requirement
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all requirements of this software version.

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

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

`BACK TO TOP <SoftwareVersion_>`_

------------

