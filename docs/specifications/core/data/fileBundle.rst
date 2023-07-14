##########
FileBundle
##########

:Semantic name: https://openminds.ebrains.eu/core/FileBundle

Structured information on a bundle of file instances.


------------

------------

Properties
##########

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `format <format_heading_>`_, `groupedBy <groupedBy_heading_>`_, `groupingType <groupingType_heading_>`_, `hash <hash_heading_>`_, `storageSize <storageSize_heading_>`_

------------

.. _contentDescription_heading:

******************
contentDescription
******************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentDescription
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short content description for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/contentType.html>`_
   :instructions: If the files within this bundle are organised and formatted according to a formal data structure, add the content type of this file bundle. Leave blank if no formal data structure has been applied to the files within this bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupedBy_heading:

*********
groupedBy
*********

Reference to the aspect used to group something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupedBy
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds-documentation.readthedocs.io/en/latest/specifications/computation/localFile.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/analysisTechnique.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/electricalStimulusType.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSystem.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/termSuggestion.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/visualStimulusType.html>`_, `BehavioralProtocol <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/behavioralProtocol.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileBundle.html>`_, `Subject <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subject.html>`_, `SubjectGroup <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectGroup.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectState.html>`_, `TissueSample <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSample.html>`_, `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleCollection.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleCollectionState.html>`_, `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleState.html>`_, `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/commonCoordinateSpace.html>`_, `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `CustomCoordinateSpace <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customCoordinateSpace.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all entities that defined which files were grouped into this file bundle. Note that the schema types of the instances stated here, need to match the ones stated under 'groupingType'.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupingType_heading:

************
groupingType
************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupingType
   :value type: | linked object array \(1-N\) of type
                | `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/fileBundleGrouping.html>`_
   :instructions: Add all grouping types that were used to define this file bundle. Note that the grouping types define the possible schema type of the instances stated under 'groupedBy'.

`BACK TO TOP <FileBundle_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/hash.html>`_
   :instructions: Add the hash that was generated for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileBundle.html>`_ or `FileRepository <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileRepository.html>`_
   :instructions: Add the file bundle or file repository this file bundle is part of.

`BACK TO TOP <FileBundle_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _storageSize_heading:

***********
storageSize
***********

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the storage size of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

