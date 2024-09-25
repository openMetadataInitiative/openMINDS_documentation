################
AmountOfChemical
################

:Semantic name: chemicals:AmountOfChemical

:Display as: Chemicals:amount of chemical


------------

------------

Properties
##########

:Required: `chemicalProduct <chemicalProduct_heading_>`_
:Optional: `amount <amount_heading_>`_

------------

.. _amount_heading:

******
amount
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/amount
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\]
   :instructions: When used in a mixture, enter the amount of the substance within the mixture (e.g., as concentration or as ratio). When used in its pure state, enter the used amount of the substance.

`BACK TO TOP <AmountOfChemical_>`_

------------

.. _chemicalProduct_heading:

***************
chemicalProduct
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/chemicalProduct
   :value type: | linked object of type
                | chemicals:ChemicalMixture \[TYPE_ERROR\], chemicals:ChemicalSubstance \[TYPE_ERROR\] or controlledTerms:MolecularEntity \[TYPE_ERROR\]
   :instructions: Add the chemical product that was used.

`BACK TO TOP <AmountOfChemical_>`_

------------

