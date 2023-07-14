######################
QuantitativeValueArray
######################

:Semantic name:: https://openminds.ebrains.eu/core/QuantitativeValueArray

A representation of an array of quantitative values, optionally with uncertainties.


------------

------------

Properties
##########

:Required: `values <values_heading_>`_
:Optional: `negativeUncertainties <negativeUncertainties_heading_>`_, `positiveUncertainties <positiveUncertainties_heading_>`_, `typeOfUncertainty <typeOfUncertainty_heading_>`_, `unit <unit_heading_>`_

------------

.. _negativeUncertainties_heading:

*********************
negativeUncertainties
*********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/negativeUncertainties
   :value type: number array \(2-N\)
   :instructions: Enter the negative uncertainties for all values. Note that the length of the arrays have to match.

`BACK TO TOP <QuantitativeValueArray_>`_

------------

.. _positiveUncertainties_heading:

*********************
positiveUncertainties
*********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/positiveUncertainties
   :value type: number array \(2-N\)
   :instructions: Enter the positive uncertainties for all values. Note that the length of the arrays have to match.

`BACK TO TOP <QuantitativeValueArray_>`_

------------

.. _typeOfUncertainty_heading:

*****************
typeOfUncertainty
*****************

Distinct technique used to quantify the uncertainty of a measurement.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/typeOfUncertainty
   :value type: | linked object of type
                | `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/typeOfUncertainty.html>`_
   :instructions: Add the type of estimation for the uncertainties.

`BACK TO TOP <QuantitativeValueArray_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement of the values and their uncertainties.

`BACK TO TOP <QuantitativeValueArray_>`_

------------

.. _values_heading:

******
values
******

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/values
   :value type: number array \(2-N\)
   :instructions: Enter all measured values.

`BACK TO TOP <QuantitativeValueArray_>`_

------------

