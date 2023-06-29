#################
ChemicalSubstance
#################

https://openminds.ebrains.eu/chemicals/ChemicalSubstance
--------------------------------------------------------

Structured information about a chemical substance.

------------

------------

**********
Properties
**********

:Required: `molecularEntity <molecularEntity_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `productSource <productSource_heading_>`_, `purity <purity_heading_>`_

------------

.. _additionalRemarks_heading:

additionalRemarks
-----------------

Mention of what deserves additional attention or notice.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter any additional remarks concering this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this chemical substance that may help you to find this instance more easily.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _molecularEntity_heading:

molecularEntity
---------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/molecularEntity
   :value type: | linked object of type
                | `MolecularEntity <https://openminds.ebrains.eu/controlledTerms/MolecularEntity>`_
   :instructions: Add the molecular entity that makes up this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _productSource_heading:

productSource
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/productSource
   :value type: | linked object of type
                | `ProductSource <https://openminds.ebrains.eu/chemicals/ProductSource>`_
   :instructions: Add the source of this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _purity_heading:

purity
------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/purity
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_ or `QuantitativeValueRange <https://openminds.ebrains.eu/core/QuantitativeValueRange>`_
   :instructions: Enter the purity of this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

