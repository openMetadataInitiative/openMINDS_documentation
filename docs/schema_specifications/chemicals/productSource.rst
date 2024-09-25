#############
ProductSource
#############

:Semantic name: chemicals:ProductSource

:Display as: Chemicals:product source


------------

------------

Properties
##########

:Required: `productName <productName_heading_>`_, `provider <provider_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `identifier <identifier_heading_>`_, `purity <purity_heading_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | core:RRID \[TYPE_ERROR\]
   :instructions: Add the globally unique and persistent digital identifier of this product.

`BACK TO TOP <ProductSource_>`_

------------

.. _identifier_heading:

**********
identifier
**********

Term or code used to identify something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/identifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier for this product, excluding its RRID (e.g., a catalog number).

`BACK TO TOP <ProductSource_>`_

------------

.. _productName_heading:

***********
productName
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/productName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this product as stated by the 'provider'.

`BACK TO TOP <ProductSource_>`_

------------

.. _provider_heading:

********
provider
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/provider
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add the party (private, commercial or industrial) that provided this product.

`BACK TO TOP <ProductSource_>`_

------------

.. _purity_heading:

******
purity
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/purity
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\] or core:QuantitativeValueRange \[TYPE_ERROR\]
   :instructions: Enter the purity of the product as stated by the 'provider'.

`BACK TO TOP <ProductSource_>`_

------------

