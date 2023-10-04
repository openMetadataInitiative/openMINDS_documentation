########################
TissueCulturePreparation
########################

:Semantic name: https://openminds.ebrains.eu/specimenPrep/TissueCulturePreparation


------------

------------

Properties
##########

:Required: `cultureMedium <cultureMedium_heading_>`_, `cultureType <cultureType_heading_>`_
:Optional: `input <input_heading_>`_, `output <output_heading_>`_

------------

.. _cultureMedium_heading:

*************
cultureMedium
*************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/cultureMedium
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/chemicals/chemicalMixture.html>`_
   :instructions: Add the culture medium used during this tissue culture preparation.

`BACK TO TOP <TissueCulturePreparation_>`_

------------

.. _cultureType_heading:

***********
cultureType
***********

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/cultureType
   :value type: | linked object of type
                | `CellCultureType <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/controlledTerms/cellCultureType.html>`_
   :instructions: Add the cell culture type of the resulting tissue cell culture.

`BACK TO TOP <TissueCulturePreparation_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object of type
                | `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/research/tissueSampleState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/research/tissueSampleCollectionState.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/research/subjectGroupState.html>`_ or `SubjectState <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/research/subjectState.html>`_
   :instructions: Add the state of the specimen before it was prepared as culture in this activity.

`BACK TO TOP <TissueCulturePreparation_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object of type
                | `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v3.0/specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the prepared tissue sample culture that resulted from this activity.

`BACK TO TOP <TissueCulturePreparation_>`_

------------

