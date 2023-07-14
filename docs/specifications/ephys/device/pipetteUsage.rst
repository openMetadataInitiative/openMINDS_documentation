############
PipetteUsage
############

:Semantic name: https://openminds.ebrains.eu/ephys/PipetteUsage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `pipetteSolution <pipetteSolution_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `chlorideReversalPotential <chlorideReversalPotential_heading_>`_, `compensationCurrent <compensationCurrent_heading_>`_, `endMembranePotential <endMembranePotential_heading_>`_, `holdingPotential <holdingPotential_heading_>`_, `inputResistance <inputResistance_heading_>`_, `labelingCompound <labelingCompound_heading_>`_, `liquidJunctionPotential <liquidJunctionPotential_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `pipetteResistance <pipetteResistance_heading_>`_, `sealResistance <sealResistance_heading_>`_, `seriesResistance <seriesResistance_heading_>`_, `spatialLocation <spatialLocation_heading_>`_, `startMembranePotential <startMembranePotential_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalLocation
   :value type: | linked object of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the pipette tip.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _chlorideReversalPotential_heading:

*************************
chlorideReversalPotential
*************************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/chlorideReversalPotential
   :value type: | embedded object array \(1-N\) of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter all chloride reversal potentials for the intracellular solution(s) of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _compensationCurrent_heading:

*******************
compensationCurrent
*******************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/compensationCurrent
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the compensation current for the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `Pipette <https://openminds-documentation.readthedocs.io/en/latest/specifications/ephys/device/pipette.html>`_
   :instructions: Add the pipette used.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _endMembranePotential_heading:

********************
endMembranePotential
********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the end of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _holdingPotential_heading:

****************
holdingPotential
****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/holdingPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the holding membrane potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _inputResistance_heading:

***************
inputResistance
***************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inputResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the input resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _labelingCompound_heading:

****************
labelingCompound
****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/labelingCompound
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/latest/specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/latest/specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the used compound for labelling e.g., a patched cell during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _liquidJunctionPotential_heading:

***********************
liquidJunctionPotential
***********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/liquidJunctionPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the liquid junction potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteResistance_heading:

*****************
pipetteResistance
*****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pipetteResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the resistance of the pipette during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteSolution_heading:

***************
pipetteSolution
***************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pipetteSolution
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/latest/specifications/chemicals/chemicalMixture.html>`_
   :instructions: Enter the solution with which the pipette was filled during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _sealResistance_heading:

**************
sealResistance
**************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/sealResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the seal resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _seriesResistance_heading:

****************
seriesResistance
****************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/seriesResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/latest/specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point that best describes the spatial location of the pipette tip during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _startMembranePotential_heading:

**********************
startMembranePotential
**********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/data/measurement.html>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the beginning of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <PipetteUsage_>`_

------------

