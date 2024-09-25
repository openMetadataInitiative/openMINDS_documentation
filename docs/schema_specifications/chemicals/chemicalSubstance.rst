#################
ChemicalSubstance
#################

:Semantic name: chemicals:ChemicalSubstance

:Display as: Chemicals:chemical substance


------------

------------

Properties
##########

:Required: `molecularEntity <molecularEntity_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `productSource <productSource_heading_>`_, `purity <purity_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this chemical substance that may help you to find this instance more easily.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _molecularEntity_heading:

***************
molecularEntity
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/molecularEntity
   :value type: | linked object of type
                | controlledTerms:MolecularEntity \[TYPE_ERROR\]
   :instructions: Add the molecular entity that makes up this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _productSource_heading:

*************
productSource
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/productSource
   :value type: | linked object of type
                | chemicals:ProductSource \[TYPE_ERROR\]
   :instructions: Add the source of this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

.. _purity_heading:

******
purity
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/purity
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the purity of this chemical substance.

`BACK TO TOP <ChemicalSubstance_>`_

------------

