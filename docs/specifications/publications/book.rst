####
Book
####

https://openminds.ebrains.eu/publications/Book
----------------------------------------------

------------

------------

**********
Properties
**********

:Required: `name <name_heading_>`_, `publicationDate <publicationDate_heading_>`_
:Optional: `IRI <IRI_heading_>`_, `abstract <abstract_heading_>`_, `author <author_heading_>`_, `citedPublication <citedPublication_heading_>`_, `copyright
   <copyright_heading_>`_, `creationDate <creationDate_heading_>`_, `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_,
   `editor <editor_heading_>`_, `funding <funding_heading_>`_, `keyword <keyword_heading_>`_, `license <license_heading_>`_, `modificationDate
   <modificationDate_heading_>`_, `publisher <publisher_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_

------------

.. _IRI_heading:

IRI
---

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted
characters to include Unicode/ISO 10646.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this creative work.

`BACK TO TOP <Book_>`_

------------

.. _abstract_heading:

abstract
--------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/abstract
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the abstract or a short description of the creative work.

`BACK TO TOP <Book_>`_

------------

.. _author_heading:

author
------

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/author
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that contributed to this creative work as authors.

`BACK TO TOP <Book_>`_

------------

.. _citedPublication_heading:

citedPublication
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/citedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_ or `ISBN <https://openminds.ebrains.eu/core/ISBN>`_
   :instructions: Add all references this creative work cites.

`BACK TO TOP <Book_>`_

------------

.. _copyright_heading:

copyright
---------

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time
period.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds.ebrains.eu/core/Copyright>`_
   :instructions: Enter the copyright information of this creative work.

`BACK TO TOP <Book_>`_

------------

.. _creationDate_heading:

creationDate
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/creationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was created, formatted as '2023-02-07'.

`BACK TO TOP <Book_>`_

------------

.. _custodian_heading:

custodian
---------

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that fulfill the role of a custodian for this creative work (e.g., a corresponding author). Custodians are typically the main
      contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the
      creative work.

`BACK TO TOP <Book_>`_

------------

.. _digitalIdentifier_heading:

digitalIdentifier
-----------------

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_ or `ISBN <https://openminds.ebrains.eu/core/ISBN>`_
   :instructions: Add the globally unique and persistent digital identifier of this creative work.

`BACK TO TOP <Book_>`_

------------

.. _editor_heading:

editor
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/editor
   :value type: | linked object array \(1-N\) of type
                | `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all persons that edited this creative work.

`BACK TO TOP <Book_>`_

------------

.. _funding_heading:

funding
-------

Money provided by a legal person for a particular purpose.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds.ebrains.eu/core/Funding>`_
   :instructions: Add all funding information of this creative work.

`BACK TO TOP <Book_>`_

------------

.. _keyword_heading:

keyword
-------

Significant word or concept that are representative of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | linked object array \(1-N\) of type
                | `ActionStatusType <https://openminds.ebrains.eu/controlledTerms/ActionStatusType>`_, `AgeCategory
                <https://openminds.ebrains.eu/controlledTerms/AgeCategory>`_, `AnalysisTechnique
                <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_, `AnatomicalAxesOrientation
                <https://openminds.ebrains.eu/controlledTerms/AnatomicalAxesOrientation>`_, `AnatomicalIdentificationType
                <https://openminds.ebrains.eu/controlledTerms/AnatomicalIdentificationType>`_, `AnatomicalPlane
                <https://openminds.ebrains.eu/controlledTerms/AnatomicalPlane>`_, `AnnotationCriteriaType
                <https://openminds.ebrains.eu/controlledTerms/AnnotationCriteriaType>`_, `AnnotationType
                <https://openminds.ebrains.eu/controlledTerms/AnnotationType>`_, `AtlasType <https://openminds.ebrains.eu/controlledTerms/AtlasType>`_,
                `AuditoryStimulusType <https://openminds.ebrains.eu/controlledTerms/AuditoryStimulusType>`_, `BiologicalOrder
                <https://openminds.ebrains.eu/controlledTerms/BiologicalOrder>`_, `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_,
                `BreedingType <https://openminds.ebrains.eu/controlledTerms/BreedingType>`_, `CellCultureType
                <https://openminds.ebrains.eu/controlledTerms/CellCultureType>`_, `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_,
                `ChemicalMixtureType <https://openminds.ebrains.eu/controlledTerms/ChemicalMixtureType>`_, `Colormap
                <https://openminds.ebrains.eu/controlledTerms/Colormap>`_, `ContributionType <https://openminds.ebrains.eu/controlledTerms/ContributionType>`_,
                `CranialWindowConstructionType <https://openminds.ebrains.eu/controlledTerms/CranialWindowConstructionType>`_, `CranialWindowReinforcementType
                <https://openminds.ebrains.eu/controlledTerms/CranialWindowReinforcementType>`_, `CriteriaQualityType
                <https://openminds.ebrains.eu/controlledTerms/CriteriaQualityType>`_, `DataType <https://openminds.ebrains.eu/controlledTerms/DataType>`_,
                `DeviceType <https://openminds.ebrains.eu/controlledTerms/DeviceType>`_, `DifferenceMeasure
                <https://openminds.ebrains.eu/controlledTerms/DifferenceMeasure>`_, `Disease <https://openminds.ebrains.eu/controlledTerms/Disease>`_,
                `DiseaseModel <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_, `EducationalLevel
                <https://openminds.ebrains.eu/controlledTerms/EducationalLevel>`_, `ElectricalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/ElectricalStimulusType>`_, `EthicsAssessment
                <https://openminds.ebrains.eu/controlledTerms/EthicsAssessment>`_, `ExperimentalApproach
                <https://openminds.ebrains.eu/controlledTerms/ExperimentalApproach>`_, `FileBundleGrouping
                <https://openminds.ebrains.eu/controlledTerms/FileBundleGrouping>`_, `FileRepositoryType
                <https://openminds.ebrains.eu/controlledTerms/FileRepositoryType>`_, `FileUsageRole
                <https://openminds.ebrains.eu/controlledTerms/FileUsageRole>`_, `GeneticStrainType
                <https://openminds.ebrains.eu/controlledTerms/GeneticStrainType>`_, `GustatoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/GustatoryStimulusType>`_, `Handedness <https://openminds.ebrains.eu/controlledTerms/Handedness>`_,
                `Language <https://openminds.ebrains.eu/controlledTerms/Language>`_, `Laterality <https://openminds.ebrains.eu/controlledTerms/Laterality>`_,
                `LearningResourceType <https://openminds.ebrains.eu/controlledTerms/LearningResourceType>`_, `MeasuredQuantity
                <https://openminds.ebrains.eu/controlledTerms/MeasuredQuantity>`_, `MetaDataModelType
                <https://openminds.ebrains.eu/controlledTerms/MetaDataModelType>`_, `ModelAbstractionLevel
                <https://openminds.ebrains.eu/controlledTerms/ModelAbstractionLevel>`_, `ModelScope <https://openminds.ebrains.eu/controlledTerms/ModelScope>`_,
                `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_, `OlfactoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OlfactoryStimulusType>`_, `OperatingDevice
                <https://openminds.ebrains.eu/controlledTerms/OperatingDevice>`_, `OperatingSystem
                <https://openminds.ebrains.eu/controlledTerms/OperatingSystem>`_, `OpticalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OpticalStimulusType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `OrganismSystem
                <https://openminds.ebrains.eu/controlledTerms/OrganismSystem>`_, `PatchClampVariation
                <https://openminds.ebrains.eu/controlledTerms/PatchClampVariation>`_, `PreparationType
                <https://openminds.ebrains.eu/controlledTerms/PreparationType>`_, `ProductAccessibility
                <https://openminds.ebrains.eu/controlledTerms/ProductAccessibility>`_, `ProgrammingLanguage
                <https://openminds.ebrains.eu/controlledTerms/ProgrammingLanguage>`_, `QualitativeOverlap
                <https://openminds.ebrains.eu/controlledTerms/QualitativeOverlap>`_, `SemanticDataType
                <https://openminds.ebrains.eu/controlledTerms/SemanticDataType>`_, `Service <https://openminds.ebrains.eu/controlledTerms/Service>`_, `SetupType
                <https://openminds.ebrains.eu/controlledTerms/SetupType>`_, `SoftwareApplicationCategory
                <https://openminds.ebrains.eu/controlledTerms/SoftwareApplicationCategory>`_, `SoftwareFeature
                <https://openminds.ebrains.eu/controlledTerms/SoftwareFeature>`_, `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_,
                `StimulationApproach <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_, `StimulationTechnique
                <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_, `SubcellularEntity
                <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `SubjectAttribute
                <https://openminds.ebrains.eu/controlledTerms/SubjectAttribute>`_, `TactileStimulusType
                <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_, `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_,
                `TermSuggestion <https://openminds.ebrains.eu/controlledTerms/TermSuggestion>`_, `Terminology
                <https://openminds.ebrains.eu/controlledTerms/Terminology>`_, `TissueSampleAttribute
                <https://openminds.ebrains.eu/controlledTerms/TissueSampleAttribute>`_, `TissueSampleType
                <https://openminds.ebrains.eu/controlledTerms/TissueSampleType>`_, `TypeOfUncertainty
                <https://openminds.ebrains.eu/controlledTerms/TypeOfUncertainty>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `UnitOfMeasurement
                <https://openminds.ebrains.eu/controlledTerms/UnitOfMeasurement>`_ or `VisualStimulusType
                <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_
   :instructions: Add all relevant keywords to this creative work either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <Book_>`_

------------

.. _license_heading:

license
-------

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object of type
                | `License <https://openminds.ebrains.eu/core/License>`_
   :instructions: Add the license of this creative work.

`BACK TO TOP <Book_>`_

------------

.. _modificationDate_heading:

modificationDate
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/modificationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was last modfied, formatted as '2023-02-07'.

`BACK TO TOP <Book_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name (or title) of this creative work.

`BACK TO TOP <Book_>`_

------------

.. _publicationDate_heading:

publicationDate
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/publicationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was published, formatted as '2023-02-07'.

`BACK TO TOP <Book_>`_

------------

.. _publisher_heading:

publisher
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/publisher
   :value type: | linked object of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the party (private or commercial) that published this creative work.

`BACK TO TOP <Book_>`_

------------

.. _versionIdentifier_heading:

versionIdentifier
-----------------

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this creative work.

`BACK TO TOP <Book_>`_

------------

