############
PipetteUsage
############

https://openminds.ebrains.eu/ephys/PipetteUsage
-----------------------------------------------

------------

------------

**********
Properties
**********

:Required: `device <device_heading_>`_, `pipetteSolution <pipetteSolution_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `chlorideReversalPotential <chlorideReversalPotential_heading_>`_, `compensationCurrent <compensationCurrent_heading_>`_, `endMembranePotential <endMembranePotential_heading_>`_, `holdingPotential <holdingPotential_heading_>`_, `inputResistance <inputResistance_heading_>`_, `labelingCompound <labelingCompound_heading_>`_, `liquidJunctionPotential <liquidJunctionPotential_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `pipetteResistance <pipetteResistance_heading_>`_, `sealResistance <sealResistance_heading_>`_, `seriesResistance <seriesResistance_heading_>`_, `spatialLocation <spatialLocation_heading_>`_, `startMembranePotential <startMembranePotential_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocation_heading:

anatomicalLocation
------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object of type
                | `CellType <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Organ <https://openminds.ebrains.eu/controlledTerms/Organ>`_, `OrganismSubstance <https://openminds.ebrains.eu/controlledTerms/OrganismSubstance>`_, `SubcellularEntity <https://openminds.ebrains.eu/controlledTerms/SubcellularEntity>`_, `UBERONParcellation <https://openminds.ebrains.eu/controlledTerms/UBERONParcellation>`_, `CustomAnatomicalEntity <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_, `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_ or `ParcellationEntityVersion <https://openminds.ebrains.eu/sands/ParcellationEntityVersion>`_
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the pipette tip.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _chlorideReversalPotential_heading:

chlorideReversalPotential
-------------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/chlorideReversalPotential
   :value type: | embedded object array \(1-N\) of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter all chloride reversal potentials for the intracellular solution(s) of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _compensationCurrent_heading:

compensationCurrent
-------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/compensationCurrent
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the compensation current for the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _device_heading:

device
------

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `Pipette <https://openminds.ebrains.eu/ephys/Pipette>`_
   :instructions: Add the pipette used.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _endMembranePotential_heading:

endMembranePotential
--------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the end of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _holdingPotential_heading:

holdingPotential
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/holdingPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the holding membrane potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _inputResistance_heading:

inputResistance
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inputResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the input resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _labelingCompound_heading:

labelingCompound
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/labelingCompound
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_, `ChemicalSubstance <https://openminds.ebrains.eu/chemicals/ChemicalSubstance>`_ or `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_
   :instructions: Add the used compound for labelling e.g., a patched cell during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _liquidJunctionPotential_heading:

liquidJunctionPotential
-----------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/liquidJunctionPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the liquid junction potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _metadataLocation_heading:

metadataLocation
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_ or `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteResistance_heading:

pipetteResistance
-----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pipetteResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `QuantitativeValueRange <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the resistance of the pipette during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteSolution_heading:

pipetteSolution
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pipetteSolution
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_
   :instructions: Enter the solution with which the pipette was filled during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _sealResistance_heading:

sealResistance
--------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/sealResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the seal resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _seriesResistance_heading:

seriesResistance
----------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/seriesResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _spatialLocation_heading:

spatialLocation
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds.ebrains.eu/sands/CoordinatePoint>`_
   :instructions: Add the coordinate point that best describes the spatial location of the pipette tip during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _startMembranePotential_heading:

startMembranePotential
----------------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds.ebrains.eu/core/Measurement>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the beginning of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _usedSpecimen_heading:

usedSpecimen
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_ or `TissueSampleState <https://openminds.ebrains.eu/core/TissueSampleState>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <PipetteUsage_>`_

------------

