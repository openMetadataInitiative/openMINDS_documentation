######################
TissueSampleCollection
######################

https://openminds.ebrains.eu/core/TissueSampleCollection
--------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `anatomicalLocation <anatomicalLocation_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `numberOfTissueSamples <numberOfTissueSamples_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concering this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _anatomicalLocation_heading:

anatomicalLocation
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_, `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `SubcellularEntity <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `UBERONParcellation <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `CustomAnatomicalEntity <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_ or `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add all anatomical entities that describe the anatomical location of this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _biologicalSex_heading:

biologicalSex
-------------

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_
   :instructions: Add the biological sex of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _laterality_heading:

laterality
----------

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds.ebrains.eu/controlledTerms/Laterality>`_
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample collection originates from.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen set that may help you to find this instance more easily.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _numberOfTissueSamples_heading:

numberOfTissueSamples
---------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/numberOfTissueSamples
   :value type: integer
   :instructions: Enter the number of tissue samples that belong to this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _origin_heading:

origin
------

Source at which something begins or rises, or from which something derives.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/origin
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_ or `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_
   :instructions: Add the biogical origin of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _species_heading:

species
-------

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object array \(1-N\) of type
                | `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_ or `Strain <https://openminds.ebrains.eu/core/Strain>`_
   :instructions: Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _studiedState_heading:

studiedState
------------

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleCollectionState <https://openminds.ebrains.eu/core/TissueSampleCollectionState>`_
   :instructions: Add all states in which this tissue sample collection was studied.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _type_heading:

type
----

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleType <https://openminds.ebrains.eu/controlledTerms/TissueSampleType>`_
   :instructions: Add the type of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

