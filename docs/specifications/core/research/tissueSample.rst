############
TissueSample
############

https://openminds.ebrains.eu/core/TissueSample
----------------------------------------------

Structured information on a tissue sample.

------------

------------

**********
Properties
**********

:Required: `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `isPartOf <isPartOf_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_

------------

.. _anatomicalLocation_heading:

anatomicalLocation
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical entities that describe the anatomical location of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

.. _biologicalSex_heading:

biologicalSex
-------------

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of this specimen.

`BACK TO TOP <TissueSample_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this specimen that is used within the corresponding data files to identify this specimen.

`BACK TO TOP <TissueSample_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleCollection.html>`_
   :instructions: Add all tissue sample collections this tissue sample is part of.

`BACK TO TOP <TissueSample_>`_

------------

.. _laterality_heading:

laterality
----------

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample originates from.

`BACK TO TOP <TissueSample_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen that may help you to find this instance more easily.

`BACK TO TOP <TissueSample_>`_

------------

.. _origin_heading:

origin
------

Source at which something begins or rises, or from which something derives.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/origin
   :value type: | linked object of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_ or `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_
   :instructions: Add the biogical origin of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

.. _species_heading:

species
-------

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/species.html>`_ or `Strain <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/strain.html>`_
   :instructions: Add the species or strain (a sub-type of a genetic variant of species) of this specimen.

`BACK TO TOP <TissueSample_>`_

------------

.. _studiedState_heading:

studiedState
------------

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all states in which this tissue sample was studied.

`BACK TO TOP <TissueSample_>`_

------------

.. _type_heading:

type
----

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | `TissueSampleType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/tissueSampleType.html>`_
   :instructions: Add the type of this tissue sample.

`BACK TO TOP <TissueSample_>`_

------------

