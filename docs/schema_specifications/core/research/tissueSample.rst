############
TissueSample
############

:Semantic name: core:TissueSample

:Display as: Core:tissue sample


------------

------------

Properties
##########

:Required: `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `isPartOf <isPartOf_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\], controlledTerms:OrganismSubstance \[TYPE_ERROR\], controlledTerms:SubcellularEntity \[TYPE_ERROR\], controlledTerms:UBERONParcellation \[TYPE_ERROR\], sands:CustomAnatomicalEntity \[TYPE_ERROR\], sands:ParcellationEntity \[TYPE_ERROR\] or sands:ParcellationEntityVersion \[TYPE_ERROR\]
   :instructions: Add all anatomical entities that describe the anatomical location of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object of type
                | controlledTerms:BiologicalSex \[TYPE_ERROR\]
   :instructions: Add the biological sex of this specimen.

`BACK TO TOP <TissueSample_>`_

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
   :instructions: Enter the identifier (or label) of this specimen that is used within the corresponding data files to identify this specimen.

`BACK TO TOP <TissueSample_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | core:TissueSampleCollection \[TYPE_ERROR\]
   :instructions: Add all tissue sample collections this tissue sample is part of.

`BACK TO TOP <TissueSample_>`_

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
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample originates from.

`BACK TO TOP <TissueSample_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen that may help you to find this instance more easily.

`BACK TO TOP <TissueSample_>`_

------------

.. _origin_heading:

******
origin
******

Source at which something begins or rises, or from which something derives.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/origin
   :value type: | linked object of type
                | controlledTerms:CellType \[TYPE_ERROR\], controlledTerms:Organ \[TYPE_ERROR\] or controlledTerms:OrganismSubstance \[TYPE_ERROR\]
   :instructions: Add the biogical origin of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object of type
                | controlledTerms:Species \[TYPE_ERROR\] or core:Strain \[TYPE_ERROR\]
   :instructions: Add the species or strain (a sub-type of a genetic variant of species) of this specimen.

`BACK TO TOP <TissueSample_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | core:TissueSampleState \[TYPE_ERROR\]
   :instructions: Add all states in which this tissue sample was studied.

`BACK TO TOP <TissueSample_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | controlledTerms:TissueSampleType \[TYPE_ERROR\]
   :instructions: Add the type of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

