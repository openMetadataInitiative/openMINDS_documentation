###########
StockNumber
###########

:Semantic name: https://openminds.ebrains.eu/core/StockNumber


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
                | `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the vendor that has the item with this identifier in stock.

`BACK TO TOP <StockNumber_>`_

------------

