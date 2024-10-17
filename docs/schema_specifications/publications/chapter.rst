#######
Chapter
#######

:Semantic name: publications:Chapter

:Display as: Publications:chapter


------------

------------

Properties
##########

:Required: `author <author_heading_>`_, `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_, `publicationDate <publicationDate_heading_>`_
:Optional: `IRI <IRI_heading_>`_, `abstract <abstract_heading_>`_, `citedPublication <citedPublication_heading_>`_, `copyright <copyright_heading_>`_, `creationDate <creationDate_heading_>`_, `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `editor <editor_heading_>`_, `funding <funding_heading_>`_, `keyword <keyword_heading_>`_, `license <license_heading_>`_, `modificationDate <modificationDate_heading_>`_, `pagination <pagination_heading_>`_, `publisher <publisher_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _abstract_heading:

********
abstract
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/abstract
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the abstract or a short description of the creative work.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add all parties that contributed to this creative work as authors.

`BACK TO TOP <Chapter_>`_

------------

.. _citedPublication_heading:

****************
citedPublication
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/citedPublication
   :value type: | linked object array \(1-N\) of type
                | core:DOI \[TYPE_ERROR\] or core:ISBN \[TYPE_ERROR\]
   :instructions: Add all references this creative work cites.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Enter the copyright information of this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _creationDate_heading:

************
creationDate
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/creationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was created, formatted as '2023-02-07'.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add all parties that fulfill the role of a custodian for this creative work (e.g., a corresponding author). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the creative work.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add the globally unique and persistent digital identifier of this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _editor_heading:

******
editor
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/editor
   :value type: | linked object array \(1-N\) of type
                | core:Person \[TYPE_ERROR\]
   :instructions: Add all persons that edited this creative work.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add all funding information of this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | publications:Book \[TYPE_ERROR\]
   :instructions: Add the book this chapter is part of.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add all relevant keywords to this creative work either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Add the license of this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _modificationDate_heading:

****************
modificationDate
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/modificationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was last modified, formatted as '2023-02-07'.

`BACK TO TOP <Chapter_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name (or title) of this creative work.

`BACK TO TOP <Chapter_>`_

------------

.. _pagination_heading:

**********
pagination
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pagination
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the page range of this chapter.

`BACK TO TOP <Chapter_>`_

------------

.. _publicationDate_heading:

***************
publicationDate
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/publicationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was published, formatted as '2023-02-07'.

`BACK TO TOP <Chapter_>`_

------------

.. _publisher_heading:

*********
publisher
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/publisher
   :value type: | linked object of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add the party (private or commercial) that published this creative work.

`BACK TO TOP <Chapter_>`_

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
   :instructions: Enter the version identifier of this creative work.

`BACK TO TOP <Chapter_>`_

------------

