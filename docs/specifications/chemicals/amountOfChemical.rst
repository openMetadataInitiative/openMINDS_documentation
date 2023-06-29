################
AmountOfChemical
################

https://openminds.ebrains.eu/chemicals/AmountOfChemical
-------------------------------------------------------

Structured information about the amount of a given chemical that was used.

------------

------------

**********
Properties
**********

:Required: `chemicalProduct <chemicalProduct_heading_>`_
:Optional: `amount <amount_heading_>`_

------------

.. _amount_heading:

amount
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/amount
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: When used in a mixture, enter the amount of the substance within the mixture (e.g., as concentration or as ratio). When used in its pure
      state, enter the used amount of the substance.

`BACK TO TOP <AmountOfChemical_>`_

------------

.. _chemicalProduct_heading:

chemicalProduct
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/chemicalProduct
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds.ebrains.eu/chemicals/ChemicalMixture>`_, `ChemicalSubstance
                <https://openminds.ebrains.eu/chemicals/ChemicalSubstance>`_ or `MolecularEntity
                <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_
   :instructions: Add the chemical product that was used.

`BACK TO TOP <AmountOfChemical_>`_

------------

