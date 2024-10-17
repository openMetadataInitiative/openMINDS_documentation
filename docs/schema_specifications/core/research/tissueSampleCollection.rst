######################
TissueSampleCollection
######################

:Semantic name: core:TissueSampleCollection

:Display as: Core:tissue sample collection


------------

------------

Properties
##########

:Required: `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `anatomicalLocation <anatomicalLocation_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `numberOfTissueSamples <numberOfTissueSamples_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all anatomical entities that describe the anatomical location of this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:BiologicalSex \[TYPE_ERROR\]
   :instructions: Add the biological sex of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | controlledTerms:Laterality \[TYPE_ERROR\]
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample collection originates from.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen set that may help you to find this instance more easily.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _numberOfTissueSamples_heading:

*********************
numberOfTissueSamples
*********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/numberOfTissueSamples
   :value type: integer
   :instructions: Enter the number of tissue samples that belong to this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _origin_heading:

******
origin
******

Source at which something begins or rises, or from which something derives.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/origin
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\] or controlledTerms:OrganismSubstance \[TYPE_ERROR\]
   :instructions: Add the biogical origin of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:Species \[TYPE_ERROR\] or core:Strain \[TYPE_ERROR\]
   :instructions: Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | core:TissueSampleCollectionState \[TYPE_ERROR\]
   :instructions: Add all states in which this tissue sample collection was studied.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:TissueSampleType \[TYPE_ERROR\]
   :instructions: Add the type of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

