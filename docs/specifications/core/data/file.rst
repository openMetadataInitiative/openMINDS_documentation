####
File
####

**************************************
https://openminds.ebrains.eu/core/File
**************************************

Structured information on a file instance that is accessible via a URL.

------------

------------

**********
Properties
**********

:Required: `IRI <IRI_heading_>`_, `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `content <content_heading_>`_, `fileRepository <fileRepository_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `specialUsageRole
   <specialUsageRole_heading_>`_, `storageSize <storageSize_heading_>`_

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
   :instructions: Enter the internationalized resource identifier of this single file.

`BACK TO TOP <File_>`_

------------

.. _content_heading:

content
-------

Something that is contained.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/content
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short content description for this file instance.

`BACK TO TOP <File_>`_

------------

.. _fileRepository_heading:

fileRepository
--------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fileRepository
   :value type: | linked object of type
                | `FileRepository <https://openminds.ebrains.eu/core/FileRepository>`_
   :instructions: Add the over all repository to which this single file belongs.

`BACK TO TOP <File_>`_

------------

.. _format_heading:

format
------

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: Add the content type of this file instance.

`BACK TO TOP <File_>`_

------------

.. _hash_heading:

hash
----

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds.ebrains.eu/core/Hash>`_
   :instructions: Add the hash that was generated for this file instance.

`BACK TO TOP <File_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_
   :instructions: Add one or several bundles in which this single file can be grouped.

`BACK TO TOP <File_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this single file.

`BACK TO TOP <File_>`_

------------

.. _specialUsageRole_heading:

specialUsageRole
----------------

Particular function of something when it is used.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specialUsageRole
   :value type: | linked object of type
                | `FileUsageRole <https://openminds.ebrains.eu/controlledTerms/FileUsageRole>`_
   :instructions: Add a special usage role for this single file.

`BACK TO TOP <File_>`_

------------

.. _storageSize_heading:

storageSize
-----------

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the storage size this file instance allocates.

`BACK TO TOP <File_>`_

------------

