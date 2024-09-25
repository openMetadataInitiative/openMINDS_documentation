##########
FileBundle
##########

:Semantic name: https://openminds.ebrains.eu/core/FileBundle

:Display as: File bundle

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

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentDescription
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter a short content description for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/contentType.html>`_
   :instructions: If the files within this bundle are organised and formatted according to a formal data structure, add the content type of this file bundle. Leave blank if no formal data structure has been applied to the files within this bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupedBy_heading:

*********
groupedBy
*********

Reference to the aspect used to group something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupedBy
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AnalysisTechnique \[TYPE_ERROR\], controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:BiologicalOrder \[TYPE_ERROR\], controlledTerms:BiologicalSex \[TYPE_ERROR\], controlledTerms:BreedingType \[TYPE_ERROR\], controlledTerms:CellCultureType \[TYPE_ERROR\], controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Disease \[TYPE_ERROR\], controlledTerms:DiseaseModel \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:GeneticStrainType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:Handedness \[TYPE_ERROR\], controlledTerms:MRIPulseSequence \[TYPE_ERROR\], controlledTerms:MRIWeighting \[TYPE_ERROR\], controlledTerms:MolecularEntity \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:OrganismSystem \[TYPE_ERROR\], controlledTerms:Species \[TYPE_ERROR\], controlledTerms:StimulationApproach \[TYPE_ERROR\], controlledTerms:StimulationTechnique \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\], controlledTerms:Technique \[TYPE_ERROR\], controlledTerms:TermSuggestion \[TYPE_ERROR\], controlledTerms:TissueSampleType \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], controlledTerms:VisualStimulusType \[TYPE_ERROR\], `LocalFile <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/localFile.html>`_, `BehavioralProtocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/behavioralProtocol.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_, `Subject <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subject.html>`_, `SubjectGroup <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectGroup.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_, `TissueSample <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSample.html>`_, `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleCollection.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleCollectionState.html>`_, `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleState.html>`_, sands:CommonCoordinateSpace \[TYPE_ERROR\], sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:CustomCoordinateSpace \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all entities that defined which files were grouped into this file bundle. Note that the schema types of the instances stated here, need to match the ones stated under 'groupingType'.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupingType_heading:

************
groupingType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupingType
   :value type: | linked object array \(1-N\) of type
                | `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/fileBundleGrouping.html>`_
   :instructions: Add all grouping types that were used to define this file bundle. Note that the grouping types define the possible schema type of the instances stated under 'groupedBy'.

`BACK TO TOP <FileBundle_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/hash.html>`_
   :instructions: Add the hash that was generated for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_ or `FileRepository <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the file bundle or file repository this file bundle is part of.

`BACK TO TOP <FileBundle_>`_

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
   :instructions: Enter the name of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _storageSize_heading:

***********
storageSize
***********

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the storage size of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

