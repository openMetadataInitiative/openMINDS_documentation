################
LearningResource
################

:Semantic name: publications:LearningResource

:Display as: Publications:learning resource


------------

------------

Properties
##########

:Required: `about <about_heading_>`_, `name <name_heading_>`_, `publicationDate <publicationDate_heading_>`_
:Optional: `IRI <IRI_heading_>`_, `abstract <abstract_heading_>`_, `author <author_heading_>`_, `citedPublication <citedPublication_heading_>`_, `copyright <copyright_heading_>`_, `creationDate <creationDate_heading_>`_, `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `editor <editor_heading_>`_, `educationalLevel <educationalLevel_heading_>`_, `funding <funding_heading_>`_, `keyword <keyword_heading_>`_, `learningOutcome <learningOutcome_heading_>`_, `license <license_heading_>`_, `modificationDate <modificationDate_heading_>`_, `order <order_heading_>`_, `prerequisite <prerequisite_heading_>`_, `publisher <publisher_heading_>`_, `requiredTime <requiredTime_heading_>`_, `topic <topic_heading_>`_, `type <type_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _about_heading:

*****
about
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/about
   :value type: | linked object array \(1-N\) of type
                | `ValidationTest <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/validationTest.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/validationTestVersion.html>`_, `WorkflowRecipe <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipe.html>`_, `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_, `Dataset <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/software.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/softwareVersion.html>`_, `WebService <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/webService.html>`_, `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/webServiceVersion.html>`_, publications:LivePaper \[TYPE_ERROR\], publications:LivePaperVersion \[TYPE_ERROR\], sands:BrainAtlas \[TYPE_ERROR\], sands:BrainAtlasVersion \[TYPE_ERROR\], sands:CommonCoordinateSpace \[TYPE_ERROR\] or sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\]
   :instructions: Add all research product (versions) this learning resource are about. Note that the learning resource should supplement the usage of the research product (versions) with e.g., instructions on their usage or additional information.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/author
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that contributed to this creative work as authors.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that fulfill the role of a custodian for this creative work (e.g., a corresponding author). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the creative work.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _educationalLevel_heading:

****************
educationalLevel
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/educationalLevel
   :value type: | linked object of type
                | controlledTerms:EducationalLevel \[TYPE_ERROR\]
   :instructions: Add the educational level that best summarizes the prerequisite of this learning resource.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _learningOutcome_heading:

***************
learningOutcome
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/learningOutcome
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description for the expected learning outcomes of this learning resource.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _order_heading:

*****
order
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/order
   :value type: integer
   :instructions: Enter the order in which this resource should appear, relative to other resources with the same topic.

`BACK TO TOP <LearningResource_>`_

------------

.. _prerequisite_heading:

************
prerequisite
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/prerequisite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any knowledge, skills, or abilities that are required to be able to use this learning resource.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

.. _publisher_heading:

*********
publisher
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/publisher
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add the party (private or commercial) that published this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _requiredTime_heading:

************
requiredTime
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/requiredTime
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the time that is required to complete this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _topic_heading:

*****
topic
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/topic
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name or a short description of the aspect of the research product that is covered by this tutorial

`BACK TO TOP <LearningResource_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | controlledTerms:LearningResourceType \[TYPE_ERROR\]
   :instructions: Add the type of this learning resource.

`BACK TO TOP <LearningResource_>`_

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

`BACK TO TOP <LearningResource_>`_

------------

