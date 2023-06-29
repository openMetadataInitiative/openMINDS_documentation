###########
FileArchive
###########

https://openminds.ebrains.eu/core/FileArchive
---------------------------------------------

------------

------------

**********
Properties
**********

:Required: `IRI <IRI_heading_>`_, `format <format_heading_>`_
:Optional: `sourceData <sourceData_heading_>`_

------------

.. _IRI_heading:

IRI
---

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted
characters to include Unicode/ISO 10646.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this file archive.

`BACK TO TOP <FileArchive_>`_

------------

.. _format_heading:

format
------

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: Add the content type of this file archive.

`BACK TO TOP <FileArchive_>`_

------------

.. _sourceData_heading:

sourceData
----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/sourceData
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_
   :instructions: Add the data that were ingested and modified to create this file archive.

`BACK TO TOP <FileArchive_>`_

------------

