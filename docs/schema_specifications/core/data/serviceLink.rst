###########
ServiceLink
###########

:Semantic name: core:ServiceLink

:Display as: Core:service link


------------

------------

Properties
##########

:Required: `dataLocation <dataLocation_heading_>`_, `openDataIn <openDataIn_heading_>`_, `service <service_heading_>`_
:Optional: `displayLabel <displayLabel_heading_>`_, `previewImage <previewImage_heading_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | core:File \[TYPE_ERROR\], core:FileArchive \[TYPE_ERROR\], core:FileBundle \[TYPE_ERROR\], core:ModelVersion \[TYPE_ERROR\], publications:LivePaperResourceItem \[TYPE_ERROR\] or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the location of the data that are linked to this specific service (e.g., stored as file (bundles) or registered as other entities such as atlas annotations).

`BACK TO TOP <ServiceLink_>`_

------------

.. _displayLabel_heading:

************
displayLabel
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/displayLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a display label for this service link.

`BACK TO TOP <ServiceLink_>`_

------------

.. _openDataIn_heading:

**********
openDataIn
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/openDataIn
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the linked data in the specified service.

`BACK TO TOP <ServiceLink_>`_

------------

.. _previewImage_heading:

************
previewImage
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/previewImage
   :value type: | linked object of type
                | core:File \[TYPE_ERROR\]
   :instructions: Add an image file to this service link that acts as a preview of its content or could function as an icon.

`BACK TO TOP <ServiceLink_>`_

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/service
   :value type: | linked object of type
                | controlledTerms:Service \[TYPE_ERROR\]
   :instructions: Add the service in which the specified data can be opened.

`BACK TO TOP <ServiceLink_>`_

------------

