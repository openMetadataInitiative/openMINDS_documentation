##########
FileBundle
##########

********************************************
https://openminds.ebrains.eu/core/FileBundle
********************************************

Structured information on a bundle of file instances.

------------

------------

**********
Properties
**********

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `format <format_heading_>`_, `groupedBy <groupedBy_heading_>`_, `groupingType
   <groupingType_heading_>`_, `hash <hash_heading_>`_, `storageSize <storageSize_heading_>`_

------------

.. _contentDescription_heading:

contentDescription
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentDescription
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short content description for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _format_heading:

format
------

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: If the files within this bundle are organised and formatted according to a formal data structure, add the content type of this file bundle.
      Leave blank if no formal data structure has been applied to the files within this bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupedBy_heading:

groupedBy
---------

Reference to the aspect used to group something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupedBy
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds.ebrains.eu/computation/LocalFile>`_, `AnalysisTechnique
                <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_, `AuditoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/AuditoryStimulusType>`_, `BiologicalOrder
                <https://openminds.ebrains.eu/controlledTerms/BiologicalOrder>`_, `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_,
                `BreedingType <https://openminds.ebrains.eu/controlledTerms/BreedingType>`_, `CellCultureType
                <https://openminds.ebrains.eu/controlledTerms/CellCultureType>`_, `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Disease
                <https://openminds.ebrains.eu/controlledTerms/Disease>`_, `DiseaseModel <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_,
                `ElectricalStimulusType <https://openminds.ebrains.eu/controlledTerms/ElectricalStimulusType>`_, `GeneticStrainType
                <https://openminds.ebrains.eu/controlledTerms/GeneticStrainType>`_, `GustatoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/GustatoryStimulusType>`_, `Handedness <https://openminds.ebrains.eu/controlledTerms/Handedness>`_,
                `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_, `OlfactoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OlfactoryStimulusType>`_, `OpticalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OpticalStimulusType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_,
                `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `OrganismSystem
                <https://openminds.ebrains.eu/controlledTerms/OrganismSystem>`_, `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_,
                `StimulationApproach <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_, `StimulationTechnique
                <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_, `SubcellularEntity
                <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `TactileStimulusType
                <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_, `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_,
                `TermSuggestion <https://openminds.ebrains.eu/controlledTerms/TermSuggestion>`_, `UBERONParcellation
                <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `VisualStimulusType
                <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_, `BehavioralProtocol
                <https://openminds.ebrains.eu/core/BehavioralProtocol>`_, `File <https://openminds.ebrains.eu/core/File>`_, `FileBundle
                <https://openminds.ebrains.eu/core/FileBundle>`_, `Subject <https://openminds.ebrains.eu/core/Subject>`_, `SubjectGroup
                <https://openminds.ebrains.eu/core/SubjectGroup>`_, `SubjectGroupState <https://openminds.ebrains.eu/core/SubjectGroupState>`_, `SubjectState
                <https://openminds.ebrains.eu/core/SubjectState>`_, `TissueSample <https://openminds.ebrains.eu/core/TissueSample>`_, `TissueSampleCollection
                <https://openminds.ebrains.eu/core/TissueSampleCollection>`_, `TissueSampleCollectionState
                <https://openminds.ebrains.eu/core/TissueSampleCollectionState>`_, `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_,
                `CommonCoordinateSpace <https://openminds.ebrains.eu/sands/CommonCoordinateSpace>`_, `CommonCoordinateSpaceVersion
                <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `CustomCoordinateSpace
                <https://openminds.ebrains.eu/sands/CustomCoordinateSpace>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_or
                `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all entities that defined which files were grouped into this file bundle. Note that the schema types of the instances stated here, need to
      match the ones stated under 'groupingType'.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupingType_heading:

groupingType
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupingType
   :value type: | linked object array \(1-N\) of type
                | `FileBundleGrouping <https://openminds.ebrains.eu/controlledTerms/FileBundleGrouping>`_
   :instructions: Add all grouping types that were used to define this file bundle. Note that the grouping types define the possible schema type of the
      instances stated under 'groupedBy'.

`BACK TO TOP <FileBundle_>`_

------------

.. _hash_heading:

hash
----

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds.ebrains.eu/core/Hash>`_
   :instructions: Add the hash that was generated for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_or `FileRepository <https://openminds.ebrains.eu/core/FileRepository>`_
   :instructions: Add the file bundle or file repository this file bundle is part of.

`BACK TO TOP <FileBundle_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _storageSize_heading:

storageSize
-----------

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the storage size of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

