###########
StockNumber
###########

:Semantic name: core:StockNumber

:Display as: Core:stock number


------------

------------

Properties
##########

:Required: `identifier <identifier_heading_>`_, `vendor <vendor_heading_>`_
:Optional:

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
   :instructions: Enter the stock number of an item provided by a store or company.

`BACK TO TOP <StockNumber_>`_

------------

.. _vendor_heading:

******
vendor
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/vendor
   :value type: | linked object of type
                | core:Organization \[TYPE_ERROR\]
   :instructions: Add the vendor that has the item with this identifier in stock.

`BACK TO TOP <StockNumber_>`_

------------

