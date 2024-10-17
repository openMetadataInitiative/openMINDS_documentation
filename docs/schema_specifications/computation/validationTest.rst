##############
ValidationTest
##############

:Semantic name: computation:ValidationTest

:Display as: Computation:validation test


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `developer <developer_heading_>`_, `fullName <fullName_heading_>`_, `hasVersion <hasVersion_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `referenceDataAcquisition <referenceDataAcquisition_heading_>`_, `scope <scope_heading_>`_, `scoreType <scoreType_heading_>`_, `studyTarget <studyTarget_heading_>`_

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
   :instructions: Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Add all parties that developed this validation test.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.

`BACK TO TOP <ValidationTest_>`_

------------

.. _hasVersion_heading:

**********
hasVersion
**********

Reference to variants of an original.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasVersion
   :value type: | linked object array \(1-N\) of type
                | computation:ValidationTestVersion \[TYPE_ERROR\]
   :instructions: Add all versions of this validation test.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <ValidationTest_>`_

------------

.. _referenceDataAcquisition_heading:

************************
referenceDataAcquisition
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/referenceDataAcquisition
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:Technique \[TYPE_ERROR\]
   :instructions: Add all acquisition techniques that were used to obtain the reference data for this validation test.

`BACK TO TOP <ValidationTest_>`_

------------

.. _scope_heading:

*****
scope
*****

Extent of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/scope
   :value type: | linked object of type
                | controlledTerms:ModelScope \[TYPE_ERROR\]
   :instructions: Add the scope of this validation test.

`BACK TO TOP <ValidationTest_>`_

------------

.. _scoreType_heading:

*********
scoreType
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/scoreType
   :value type: | linked object of type
                | controlledTerms:DifferenceMeasure \[TYPE_ERROR\]
   :instructions: Add the type of score calculated in this validation test.

`BACK TO TOP <ValidationTest_>`_

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
   :instructions: Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <ValidationTest_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:BiologicalOrder \[TYPE_ERROR\], controlledTerms:BiologicalSex \[TYPE_ERROR\], controlledTerms:BreedingType \[TYPE_ERROR\], controlledTerms:CellCultureType \[TYPE_ERROR\], controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Disease \[TYPE_ERROR\], controlledTerms:DiseaseModel \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:GeneticStrainType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:Handedness \[TYPE_ERROR\], controlledTerms:MolecularEntity \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:OrganismSystem \[TYPE_ERROR\], controlledTerms:Species \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\], controlledTerms:TermSuggestion \[TYPE_ERROR\], controlledTerms:TissueSampleType \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], controlledTerms:VisualStimulusType \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all study targets of this validation test.

`BACK TO TOP <ValidationTest_>`_

------------

