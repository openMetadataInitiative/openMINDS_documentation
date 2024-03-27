###################
TissueSampleSlicing
###################

:Semantic name: https://openminds.ebrains.eu/specimenPrep/TissueSampleSlicing

:Display as: Tissue sample slicing


------------

------------

Properties
##########

:Required: `device <device_heading_>`_
:Optional: `input <input_heading_>`_, `output <output_heading_>`_, `temperature <temperature_heading_>`_, `tissueBathSolution <tissueBathSolution_heading_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object of type
                | `SlicingDeviceUsage <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/specimenPrep/device/slicingDeviceUsage.html>`_
   :instructions: Add the device used to slice the tissue sample.

`BACK TO TOP <TissueSampleSlicing_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the specimen that was sliced during this activity.

`BACK TO TOP <TissueSampleSlicing_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample slice or collection of slices that resulted from this activity.

`BACK TO TOP <TissueSampleSlicing_>`_

------------

.. _temperature_heading:

***********
temperature
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/temperature
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the temperature at which the tissue sample was sliced during the activity.

`BACK TO TOP <TissueSampleSlicing_>`_

------------

.. _tissueBathSolution_heading:

******************
tissueBathSolution
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/tissueBathSolution
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/chemicals/chemicalMixture.html>`_
   :instructions: Add the chemical mixture used as bath solution during this activity.

`BACK TO TOP <TissueSampleSlicing_>`_

------------

